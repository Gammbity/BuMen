from rest_framework import serializers
from user.models import UserModel

class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    password = serializers.CharField()
    class Meta: 
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'password2']
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs
    
    def create(self, validated_data):
        password2 = validated_data.pop('password2')
        user = UserModel.objects.create_user(**validated_data)
        return user