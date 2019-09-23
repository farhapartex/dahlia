from rest_framework import serializers
from .models import *


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class PublicMenuSerializer(serializers.ModelSerializer):
    #parent_menu = serializers.SerializerMethodField()
    submenus = serializers.SerializerMethodField()

    def get_submenus(self, obj):
        menus =  MenuItem.objects.filter(parent_menu=None)
        serializer = RecursiveField(menus,many=True)
        return serializer.data

    class Meta:
        model = MenuItem
        fields = ("id","name","url","allow_submenu","parent_menu","submenus") 
            
