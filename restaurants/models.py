from django.db import models
from users.models import User
from food_delivery_api_drf.constants import RESTAURANT_TYPES, MENU_CATEGORIES


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    restaurant_type = models.CharField(
        max_length=10, choices=RESTAURANT_TYPES, default='other')
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='restaurant')

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100)
    menu_category = models.CharField(
        max_length=20, choices=MENU_CATEGORIES, default='main_course')
    modifiers = models.TextField(blank=True)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='menu')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='menu_item')

    def __str__(self):
        return self.name
