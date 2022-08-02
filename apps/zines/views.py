from django.shortcuts import render
from apps.zines.models import Zine
from apps.zines.serializers import ZineSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse

class HomeView(APIView):

   def get(self, request, format=None):
      return JsonResponse({"message":
      'Hello World'})

class ZineViewSet(ModelViewSet):
   queryset = Zine.objects.all()
   serializer_class = ZineSerializer
   pagination_class = PageNumberPagination
