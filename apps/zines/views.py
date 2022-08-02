from django.shortcuts import render
from rest_framework.views import APIView  
from django.http import JsonResponse  

class HomeView(APIView):  

 def get(self, request, format=None):
    return JsonResponse({"message":
    'Hello World'})
