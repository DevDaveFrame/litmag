from apps.zines.models import Zine, Genre, UserProfile, Work
from apps.zines.serializers import ZineSerializer, GenreSerializer, UserProfileSerializer, WorkSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse


class HomeView(APIView):

    def get(self, request, format=None):
        return JsonResponse({'message':
                             'Hello World'})


class ZineViewSet(ModelViewSet):
    queryset = Zine.objects.all()
    serializer_class = ZineSerializer
    pagination_class = PageNumberPagination


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = PageNumberPagination


class WorkViewSet(ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    pagination_class = PageNumberPagination
