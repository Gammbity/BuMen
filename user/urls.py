from django.urls import path
from user import views

urlpatterns = [
    # path('user/create/', views.UserCreateView.as_view()), 
    path('registr/', views.RegistrationView.as_view()), 
    path('me/', views.MeView.as_view()),  
]
