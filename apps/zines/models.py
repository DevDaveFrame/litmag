from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=60, blank=False, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Zine(models.Model):
    genres = models.ManyToManyField('Genre', blank=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'


class UserProfile(models.Model):
    class UserRole(models.TextChoices):
        READER = 'Reader'
        EDITOR = 'Editor'
        AUTHOR = 'Author'
        SUBSCRIBER = 'Subscriber'
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=60, blank=False, null=True)
    role = models.CharField(choices=UserRole.choices, default=UserRole.SUBSCRIBER, max_length=60, blank=False, null=True)
    pronouns = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} ({self.pronouns})'


class Work(models.Model):
    author = models.ForeignKey('UserProfile', blank=False, null=False, on_delete=models.CASCADE)
    genres = models.ManyToManyField('Genre')
    placements = models.ManyToManyField('Zine', blank=True)
    abstract = models.TextField(blank=True, null=False)
    body = models.TextField(blank=True, null=False)
    title = models.CharField(max_length=100, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} by {self.author.name}'
