from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
# Create your views here.

class PublicCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = PublicCategorySerializer

class PublicTagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = PublicTagSerializer

class PublicPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = FlatPostSerializer

    def get_queryset(self):
        return Post.objects.filter(published=True)
    
    def get_serializer_class(self):
        if self.action == "list":
            return FlatPostSerializer
        return PublicPostSerializer
