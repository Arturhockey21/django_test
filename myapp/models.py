from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, related_name='owned_products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Lesson(models.Model):
    products = models.ManyToManyField(Product, related_name='lessons')
    title = models.CharField(max_length=200)
    video_link = models.URLField()
    duration = models.PositiveIntegerField()

class ProductAccess(models.Model):
    user = models.ForeignKey(User, related_name='product_accesses', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='accesses', on_delete=models.CASCADE)

class LessonView(models.Model):
    user = models.ForeignKey(User, related_name='lesson_views', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='views', on_delete=models.CASCADE)
    view_duration = models.PositiveIntegerField()
    STATUS_CHOICES = [('WATCHED', 'Watched'), ('UNWATCHED', 'Unwatched')]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

