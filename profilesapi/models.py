from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
     """Manager for user profile"""

    def create_user(self,email,name,password=None):
        """create new user profiles"""

        if not email:
            raise ValueError("user must have an email address")

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_supperuser(self,email,name,password):
        """" Create and  save new superuser with details"""
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_saff=True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database models for user in the system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_saff=models.BooleanField(default=False)

    object=UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Retrieve string representation of our user"""
        return self.email