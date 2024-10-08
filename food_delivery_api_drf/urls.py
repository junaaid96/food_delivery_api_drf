from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('restaurants/', include('restaurants.urls')),
    path('orders/', include('orders.urls')),
]
