from django.contrib import admin
from apps.users.models import User, Profile

# Register your models here.

@admin.register(User,Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = []
    list_editable = []
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = []
    list_editable = []