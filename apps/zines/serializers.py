from rest_framework import serializers
from .models import Zine, Genre, UserProfile, Work

class ZineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zine
        fields = '__all__'