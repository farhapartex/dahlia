from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(SocialMediaInfo)
class SocialMediaInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass
