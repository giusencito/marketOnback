from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from  django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('No email provided')
        if not name:
            raise ValueError('No name provided')
        email = self.normalize_email
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=30,unique=True)
    userName = models.CharField(max_length=30)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['userName']
    def get_full_name(self):
        return self.userName
    def __str__(self):
        return self.email