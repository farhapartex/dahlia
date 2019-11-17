from rest_framework import serializers
from media_browser.serializers import FlatPublicMediaSerializer
from cms_admin.models import Notification
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
    site_logo = serializers.SerializerMethodField()
    site_favicon = serializers.SerializerMethodField()

    def get_menus(self, obj):
        menus = MenuItem.objects.filter(parent_menu=None)
        serializer = PublicMenuItemSerializer(menus, many=True)
        return serializer.data
    
    def get_site_logo(self, model):
        image = model.site_logo
        return FlatPublicMediaSerializer(image).data
    
    def get_site_favicon(self, model):
        image = model.site_logo
        return FlatPublicMediaSerializer(image).data
        

    class Meta:
        model = SiteInformation
        fields = ("id", "site_name","site_logo","site_favicon", "menus")


class ContactSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        contact = Contact.objects.create(**validated_data)
        notification = Notification(content_object=contact)
        notification.save()
        return contact

    class Meta:
        model = Contact
        fields = ("id","name","email","message")
