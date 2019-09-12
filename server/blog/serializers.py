from rest_framework import serializers
from .models import *

class PublicCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)

class PublicTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)


class FlatPostSerializer(serializers.ModelSerializer):
    category = PublicCategorySerializer()
    tags = PublicTagSerializer(many=True)
    class Meta:
        model = Post
        fields = ("id","title","category","tags","created_at")

class PublicPostSerializer(serializers.ModelSerializer):
    category = PublicCategorySerializer()
    tags = PublicTagSerializer(many=True)
    class Meta:
        model = Post
        fields = ("id","title","subtitle","body","category","tags","published","created_at")