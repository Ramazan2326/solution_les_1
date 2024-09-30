from django.contrib import admin
from django.urls import path, include
from core.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('personal_cabinet/', include('personal_cabinet.urls')),
    path('products_catalog/', include('products_catalog.urls')),
    path('shopping_cart/', include('shopping_cart.urls')),
]
