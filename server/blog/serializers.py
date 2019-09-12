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

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ("id","type","amount")

class ChildCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id","parent","body","created_at","updated_at")

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(
            value,
            context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    class Meta:
        model = Comment
        fields = ("id","parent","children","body","created_at","updated_at")

class PublicPostSerializer(serializers.ModelSerializer):
    category = PublicCategorySerializer()
    tags = PublicTagSerializer(many=True)
    reacts = ReactSerializer(many=True)
    # comments = CommentSerializer(many=True)
    comments= serializers.SerializerMethodField()

    def get_comments(self,obj):
         post_comment = Comment.objects.filter(post = obj.id, parent = None)
         serializer = CommentSerializer(post_comment,many=True)
         return serializer.data

    class Meta:
        model = Post
        fields = ("id","title","subtitle","body","category","tags","reacts","comments","published","created_at")