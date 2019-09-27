from rest_framework import serializers
from .models import *


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class PublicMenuItemSerializer(serializers.ModelSerializer):
    submenus = RecursiveField(many=True)

    class Meta:
        model = MenuItem
        fields = ("id", "name", "url", "allow_submenu", "parent_menu", "submenus")


class PublicSiteInformationSerializer(serializers.ModelSerializer):
    # menus = PublicMenuItemSerializer(many=True)
    menus = serializers.SerializerMethodField()

    def get_menus(self, obj):
        menus = MenuItem.objects.filter(parent_menu=None)
        serializer = PublicMenuItemSerializer(menus, many=True)
        return serializer.data

    class Meta:
        model = SiteInformation
        fields = ("id", "site_name", "menus")


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("id","name","email","message")
