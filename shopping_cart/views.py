from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Вы перешли в корзину')


def delete_cart(request):
    return HttpResponse('Вы удалили корзину')


def buy_cart(request):
    return HttpResponse('Вы выкупили все товары в Вашей корзине')
