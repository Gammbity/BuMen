from django.shortcuts import render
from rest_framework import generics
from course import models
from course import serializers

class UserLessonView(generics.ListAPIView):
    queryset = models.UserLessonModel.objects.all()
    serializer_class = serializers.UserLessonSerializer