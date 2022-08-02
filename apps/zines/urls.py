from rest_framework import routers
from .views import ZineViewSet, GenreViewSet, UserProfileViewSet, WorkViewSet

zines_router = routers.DefaultRouter()
zines_router.register(r'zines', ZineViewSet, basename='zines')

genres_router = routers.DefaultRouter()
genres_router.register(r'genres', GenreViewSet, basename='genres')

user_profiles_router = routers.DefaultRouter()
user_profiles_router.register(r'user_profiles', UserProfileViewSet, basename='user_profiles')

works_router = routers.DefaultRouter()
works_router.register(r'works', WorkViewSet, basename='works')
