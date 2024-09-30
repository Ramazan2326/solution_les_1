from django.urls import path
from personal_cabinet.views import index, delete_profile, set_profile

urlpatterns = [
    path('', index),
    path('delete/', delete_profile),
    path('set_profile/', set_profile),
]
