from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=60, blank=False, null=True)

class Zine(models.Model):
    genres = models.ManyToManyField('Genre', blank=False)
    name = models.CharField(max_length=100, blank=False, null=True)
    
class UserProfile(models.Model):
    class UserRole(models.TextChoices):
        READER = "Reader"
        EDITOR = "Editor"
        AUTHOR = "Author"
        SUBSCRIBER = "Subscriber"
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=60, blank=False, null=True)
    role = models.CharField(choices=UserRole.choices, default=UserRole.SUBSCRIBER)
    pronouns = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(blank=False, null=True)

class Work(models.Model):
    author = models.ForeignKey('UserProfile', blank=False, null=False, on_delete=models.CASCADE)
    genres = models.ManyToManyField('Genre')
    abstract = models.TextField(blank=True, null=False)
    body = models.TextField(blank=True, null=False)
    
