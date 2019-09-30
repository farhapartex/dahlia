from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(CustomModel)
class StreamFieldAdmin(admin.ModelAdmin):
    pass
