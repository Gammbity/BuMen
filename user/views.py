from rest_framework import generics 
from user.models import UserModel
from rest_framework.response import Response
from rest_framework import status
from user import serializers

class MeView(generics.ListAPIView):
    serializer_class = serializers.MeSerializer

    def get_queryset(self):
        user = self.request.user
        return UserModel.objects.filter(id=user.id)
    
class RegistrationView(generics.GenericAPIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.save(), status=status.HTTP_201_CREATED)


# class UserCreateView(generics.CreateAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = serializers.UserCreateSerializer
