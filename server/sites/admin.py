from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    pass
