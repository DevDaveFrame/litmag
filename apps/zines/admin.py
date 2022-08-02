from django.contrib import admin
from .models import Genre, Zine, UserProfile, Work

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Zine)
class ZineAdmin(admin.ModelAdmin):
    pass

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass
