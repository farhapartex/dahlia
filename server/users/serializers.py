from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class FlatUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","first_name","last_name","email")


class PublicProfileSerializer(serializers.ModelSerializer):
    user = FlatUserSerializers()
    class Meta:
        model = Profile
        read_only_fields = ('user',)
        fields = ("id","user","avatar","bio","about","mobile")