from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from restaurants.models import Restaurant, MenuItem
from food_delivery_api_drf.constants import ORDER_STATUS, PAYMENT_METHODS

User = get_user_model()

class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHODS)
    status = models.CharField(
        max_length=20, choices=ORDER_STATUS, default='pending')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='order')
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='order')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.restaurant} - {self.status} - {self.menu_item} - {self.quantity}'

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Check if the menu item belongs to the restaurant
        if self.menu_item.restaurant != self.restaurant:
            raise ValidationError(
                "This item is not available in the selected restaurant.")

        # Check if the quantity is at least 1
        if self.quantity < 1:
            raise ValidationError("At least one item must be ordered.")

        # Check if the stock is available
        if self.menu_item.available_stock < self.quantity:
            raise ValidationError("This item is out of stock.")

        super().save(*args, **kwargs)
        menu_item = self.menu_item
        menu_item.available_stock -= self.quantity
        menu_item.order_count += self.quantity
        menu_item.save()