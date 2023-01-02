from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import (Profile)


@admin.register(Profile)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['user','is_email_verified', 'email_token', 'profile_image']

