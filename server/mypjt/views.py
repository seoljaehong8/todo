from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from django.core.cache import cache

def index(request):   

    cache.set('key','hello',timeout=10)
    print('1111111111111111111111111111111111111111111111111111111111111111111111111')

    print(cache.get('key'))

    print('2222222222222222222222222222222222222222222222222222222222222222222222222')

    return HttpResponse({'make data in elasticache redis'},status=200)