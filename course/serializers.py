from course import models
from rest_framework import serializers

class LessonThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LessonThemeModel
        fields = ['title', 'photo', 'author', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryModel
        fields = ['name']

class UserLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserLessonModel
        fields = ['lesson']