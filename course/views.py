from rest_framework import generics
from course import models
from course import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status

class ClubView(generics.ListAPIView):
    serializer_class = serializers.ClubSerializer

    def get_queryset(self):
        theme_id = self.kwargs['theme_id']
        queryset = models.ClubModel.objects.filter(theme=theme_id)
        return queryset
    
    def list(self, request, *args, **kwargs):
        clubs = self.get_queryset()
        data = []
        if clubs:
            for club in clubs:
                data.append({
                    'theme': club.theme.title,
                    'title': club.title
                })
            return Response(data, status=status.HTTP_200_OK)

class VacansyListAPIView(generics.ListAPIView):
    serializer_class = serializers.VacansySerializer

    def get_queryset(self):
        theme_id = self.kwargs['theme_id']
        lesson_type = self.kwargs['lesson_type']
        queryset = models.VacansyModel.objects.filter(lesson__theme=theme_id, lesson__type=lesson_type)
        return queryset
    
    def list(self, request, *args, **kwargs):
        vacansies = self.get_queryset()
        if vacansies:
            data = []
            for vacansy in vacansies:
                data.append({
                    'title': vacansy.title,
                    'category': vacansy.category.name,
                    'company_name': vacansy.company_name,
                    'description': vacansy.description,
                    'salary': vacansy.salary
                })
            return Response(data, status=status.HTTP_200_OK)
        
class StageView(generics.ListAPIView):
    serializer_class = serializers.StageSerializer

    def get_queryset(self):
        theme_id = self.kwargs['theme_id']
        lesson_type = self.kwargs['lesson_type']
        queryset = models.StageModel.objects.filter(lesson=lesson_type, lesson__theme=theme_id)
        return queryset
    
    def list(self, request, *args, **kwargs):
        stages = self.get_queryset()
        data = []
        if stages:
            for stage in stages:
                theme, type, stage = str(stage).split('|')
                data.append({
                    'theme': theme,
                    'type': type,
                    'stage': stage
                })
            return Response(data, status=status.HTTP_200_OK)
        
class LessonView(generics.ListAPIView):
    serializer_class = serializers.LessonSerializer

    def get_queryset(self):
        theme_id = self.kwargs['theme_id']
        lesson_type = self.kwargs['lesson_type']
        queryset = models.LessonModel.objects.filter(theme=theme_id, type=lesson_type)
        return queryset

    def list(self, request, *args, **kwargs):
        lessons = self.get_queryset()
        if lessons:
            theme, type = str(lessons[0]).split("|")
            return Response({
                'theme': theme,
                'type': type
            }, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class LessonThemesView(generics.ListAPIView):
    queryset = models.LessonThemeModel.objects.all()
    serializer_class = serializers.LessonThemeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']

class CategoryView(generics.ListAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']

class UserLessonView(generics.ListAPIView):
    queryset = models.UserLessonModel.objects.all()
    serializer_class = serializers.UserLessonSerializer