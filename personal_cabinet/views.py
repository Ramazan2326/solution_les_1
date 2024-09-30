from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Вы перешли в личный кабинет')

def set_profile(request):
    return HttpResponse('Здесь можно будет настроить профиль')

def delete_profile(request):
    return HttpResponse('Упс, кажется Вы хотите удалить свой профиль...')