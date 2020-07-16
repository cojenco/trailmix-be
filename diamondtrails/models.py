from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
# Create your models here.

# class UserManager(BaseUserManager):
#     def _create_user(self, email, password, is_staff, is_superuser):
#         if not email:
#             raise ValueError('Users must have an email address')
#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             is_staff=is_staff,
#             is_active=True,
#             is_superuser=is_superuser,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_user(self, email, password):
#         return self._create_user(email, password, False, False)

#     def create_superuser(self, email, password):
#         superuser = self._create_user(email, password, True, True)
#         superuser.save(using=self._db)
#         return superuser


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=254, unique=True)
#     username = models.CharField(max_length=150)
#     provider = models.CharField(max_length=150)
#     uid = models.BigIntegerField()
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def get_absolute_url(self):
#         return "/users/%i/" % (self.pk)


class StatusUpdate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    external_id = models.BigIntegerField()


class Subscription(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.BigIntegerField()
    phone = models.CharField(max_length = 15)
    trail = models.CharField(max_length = 150)


class USstate(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=2)
    lat = models.DecimalField(max_digits=22, decimal_places=16)
    lng = models.DecimalField(max_digits=22, decimal_places=16)
    
    def __str__(self):
        return self.abbr