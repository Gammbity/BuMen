from rest_framework import generics 
from user.models import UserModel
from user.serializers import UserCreateSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserCreateSerializer
