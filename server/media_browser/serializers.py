from rest_framework import serializers
from .models import *

class MediaImagePrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaImage
        fields = ("__all__")