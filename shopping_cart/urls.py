from django.urls import path
from shopping_cart.views import index, delete_cart, buy_cart

urlpatterns = [
    path('', index),
    path('delete/', delete_cart),
    path('buy_all/', buy_cart),
]
