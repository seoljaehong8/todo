from rest_framework import status
from django.http import HttpResponse

def index(request):
    return HttpResponse({'ok123'},status=200)