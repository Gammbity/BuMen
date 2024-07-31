from django.urls import path
from course import views

urlpatterns = [
    path('user/lessons/', views.UserLessonView.as_view()),
    path('categories/', views.CategoryView.as_view()),
    path('themes/', views.LessonThemesView.as_view()),
    path('themes/<int:theme_id>/lessons/<str:lesson_type>/', views.LessonView.as_view()),
    path('themes/<int:theme_id>/<int:lesson_type>/stages/', views.StageView.as_view())
]
