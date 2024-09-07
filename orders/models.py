from django.db import models
from users.models import User
from restaurants.models import Restaurant
from food_delivery_api_drf.constants import ORDER_STATUS, PAYMENT_METHODS


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='order')
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='order')
    status = models.CharField(
        max_length=20, choices=ORDER_STATUS, default='pending')
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHODS)
    total_items = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.restaurant} - {self.status}'

    class Meta:
        ordering = ['-created_at']
