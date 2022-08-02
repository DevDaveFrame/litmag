from rest_framework import serializers
from .models import Zine, Genre, UserProfile, Work


class ZineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zine
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'
