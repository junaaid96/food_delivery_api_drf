from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework import permissions
from food_delivery_api_drf.permissions import IsOwner, IsEmployee


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'list':
            permission_classes = [IsOwner | IsEmployee]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
