from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Please enter an email address')
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user=self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=15)
    is_business = models.BooleanField(default=False)

    # 권한
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # username을 email로
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return f'email {self.email}, nickname {self.nickname}'
