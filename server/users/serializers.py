from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class FlatUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","first_name","last_name","email")

class SocialMediaPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaInfo
        fields = ("id","website","facebook","twitter","linkedin","instagram","stackoverflow","github")

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ("name",)

class PublicProfileSerializer(serializers.ModelSerializer):
    user = FlatUserSerializers()
    socialMedia = SocialMediaPublicSerializer()
    skills = SkillSerializer(many=True)
    
    class Meta:
        model = Profile
        read_only_fields = ('user','skills')
        fields = ("id","user","avatar","bio","about","mobile","socialMedia","skills")