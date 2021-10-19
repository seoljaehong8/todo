from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from django.core.cache import cache

def index(request):   

    cache.set('test','from elasticache redis',timeout=10)

    print(cache.get('test'))


    return HttpResponse({'make data in elasticache redis'},status=200)