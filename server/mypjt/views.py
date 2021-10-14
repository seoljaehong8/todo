from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse({'ok123'},status=200)