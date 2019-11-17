from rest_framework import serializers
from .models import *

class MediaImagePrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaImage
        fields = ("__all__")


class FlatPublicMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaImage
        fields = ("id","image","width","height")