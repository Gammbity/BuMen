from course import models
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryModel
        fields = ['name']

class UserLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserLessonModel
        fields = ['lesson']