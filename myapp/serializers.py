from rest_framework import serializers
from .models import Product, Lesson, LessonView

class LessonSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    view_duration = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_link', 'duration', 'status', 'view_duration']

    def get_status(self, obj):
        try:
            view = LessonView.objects.get(user=self.context['request'].user, lesson=obj)
            return view.status
        except LessonView.DoesNotExist:
            return "UNWATCHED"

    def get_view_duration(self, obj):
        try:
            view = LessonView.objects.get(user=self.context['request'].user, lesson=obj)
            return view.view_duration
        except LessonView.DoesNotExist:
            return 0

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'owner']
