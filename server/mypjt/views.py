from rest_framework import status
from rest_framework.response import Response

def index(request):
    return Response({'success : 성공!!'},status=status.HTTP_200_SUCCESS)