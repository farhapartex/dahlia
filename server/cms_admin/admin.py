from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(SystemPermission)
class SystemPermissionAdmin(admin.ModelAdmin):
    pass
