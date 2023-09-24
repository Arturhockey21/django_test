from django.urls import path
from . import views

urlpatterns = [
    path('lessons_for_user/', views.AllLessonsForUser.as_view(), name='all-lessons-for-user'),
    path('lessons_by_product/<int:product_id>/', views.LessonsByProduct.as_view(), name='lessons-by-product'),
    path('product_statistics/', views.ProductStatistics.as_view(), name='product-statistics')
]
