from course import models
from rest_framework import serializers

class UserLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserLessonModel
        fields = ['lesson']