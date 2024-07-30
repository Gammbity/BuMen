from rest_framework import serializers
from user.models import UserModel
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'full_name', 'balance', 'is_pro', 'pro_finish_at']

class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def validate_email(self, value):
        print(value)
        user_exists = UserModel.objects.filter(email=value).exists()
        if user_exists:
            raise ValidationError(_(f"Ushbu {value} email band!"))
        return value
    
    def validate(self, data):
        try:
            user = UserModel(first_name=data['first_name'], last_name=data['last_name'])
            validate_password(data['password'], user)
        except DjangoValidationError as e:
            raise ValidationError({
                'password': list(e.messages)
            })
        return data
    
    def create(self, validated_data):
        user = UserModel.objects.create_user(
            email=validated_data['email'], 
            password=validated_data['password'],
            first_name=validated_data['first_name'], 
            last_name=validated_data['last_name']
        )
        refresh_token = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token)
        }

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
    