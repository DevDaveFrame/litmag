from rest_framework import routers
from .views import ZineViewSet, GenreViewSet, UserProfileViewSet, WorkViewSet

zines_router = routers.DefaultRouter()
zines_router.register(r'zines', ZineViewSet, basename='zines')
