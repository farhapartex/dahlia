from django.contrib import admin
from .models import *

@admin.register(MediaImage)
class MediaImageAdmin(admin.ModelAdmin):
    pass
