from rest_framework import viewsets
from .models import Restaurant, Menu, MenuItem
from .serializers import RestaurantSerializer, MenuSerializer, MenuItemSerializer
from food_delivery_api_drf.permissions import IsOwner, IsEmployee
from rest_framework import permissions


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_permissions(self):
        # only owner can create a restaurant
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        # only owner can update, partial update, and delete a restaurant
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwner]
        else:
            # anyone can view a restaurant
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        # only owner and employee can create a menu
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        # only owner and employee can update, partial update, and delete a menu
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwner, IsEmployee]
        else:
            # anyone can view a menu
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        # only owner and employee can create a menu item
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        # only owner and employee can update, partial update, and delete a menu item
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwner, IsEmployee]
        else:
            # anyone can view a menu item
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
