from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
