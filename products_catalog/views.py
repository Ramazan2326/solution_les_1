from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(f'Здесь – каталог товаров!')


def get_book_cat(request):
    return HttpResponse('Вы перешли в каталог книг')


def get_gadget_cat(request):
    return HttpResponse('Вы перешли в каталог гаджетов')


def get_vehicles_cat(request):
    return HttpResponse('Теперь Вы в категории транспорта')