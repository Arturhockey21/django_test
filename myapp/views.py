from django.shortcuts import render

from rest_framework import views, response, permissions
from django.db.models import Sum
from .models import Product, Lesson, LessonView, ProductAccess
from .serializers import LessonSerializer, ProductSerializer

class LessonsByProduct(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        lessons = Lesson.objects.filter(products__in=[product])
        serializer = LessonSerializer(lessons, many=True, context={'request': request})
        return response.Response(serializer.data)

class AllLessonsForUser(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_products = ProductAccess.objects.filter(user=request.user).values_list('product', flat=True)
        lessons = Lesson.objects.filter(products__in=user_products)
        serializer = LessonSerializer(lessons, many=True, context={'request': request})
        return response.Response(serializer.data)

class ProductStatistics(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        data = []
        total_users = User.objects.count()
        
        for product in products:
            lessons = Lesson.objects.filter(products=product)
            total_lessons_views = LessonView.objects.filter(lesson__in=lessons).count()
            total_view_time = LessonView.objects.filter(lesson__in=lessons).aggregate(Sum('view_duration'))['view_duration__sum'] or 0
            total_students = ProductAccess.objects.filter(product=product).count()
            access_rate = (total_students / total_users) * 100

            data.append({
                "product_id": product.id,
                "product_name": product.name,
                "lessons_watched": total_lessons_views,
                "total_view_time": total_view_time,
                "total_students": total_students,
                "access_rate": access_rate
            })
        
        return response.Response(data)

