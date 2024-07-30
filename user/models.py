from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class UserModel(AbstractUser, BaseModel):
    choice = (
        (1, _('pro')),
        (2, _('oddiy'))
    )
    
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    telegram_id = models.CharField(max_length=255, null=True, blank=True)
    balance = models.PositiveBigIntegerField(default=50000)
    is_pro = models.CharField(max_length=255, choices=choice)
    pro_finish_at = models.DateTimeField(null=True)
    lang = models.CharField(max_length=2)
    score = models.PositiveIntegerField(default=0)
    
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('foydalanuvchi')
        verbose_name_plural = _('foydalanuvchilar')
