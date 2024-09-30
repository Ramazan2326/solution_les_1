from django.urls import path
from products_catalog.views import index, get_book_cat, \
    get_gadget_cat, get_vehicles_cat

urlpatterns = [
    path('', index),
    path('books/', get_book_cat),
    path('gadgets/', get_gadget_cat),
    path('vehicles/', get_vehicles_cat),
]
