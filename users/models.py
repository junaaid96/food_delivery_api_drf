from django.db import models
from django.contrib.auth.models import AbstractUser
from food_delivery_api_drf.constants import USER_ROLES


class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    role = models.CharField(
        max_length=10, choices=USER_ROLES, default='customer')
