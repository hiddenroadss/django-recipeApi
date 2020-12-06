from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
    PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create and save superuser"""
        user = self.create_user(email, password)
        user.is_stuff = True
        user.is_superuser = True
        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support using email instead of username"""
    email = models.EmailField('Email', max_length=255, unique=True)
    name = models.CharField('Name', max_length=255)
    is_active = models.BooleanField('Active', default=True)
    is_stuff = models.BooleanField('Is stuff', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
