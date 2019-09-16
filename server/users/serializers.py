from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class FlatUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","first_name","last_name","email")
        # fields = ("__all__")

class SocialMediaPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaInfo
        fields = ("id","type","url")

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ("name",)

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ("id","degree","institution","session")

class PublicProfileSerializer(serializers.ModelSerializer):
    user = FlatUserSerializers()
    socialMedias = SocialMediaPublicSerializer(many=True)
    skills = SkillSerializer(many=True)
    educations = EducationSerializer(many=True)

    class Meta:
        model = Profile
        read_only_fields = ('user','skills')
        fields = ("id","user","avatar","bio","about","mobile","socialMedias","skills","educations")