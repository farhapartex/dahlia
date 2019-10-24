from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters
from rest_framework import generics, viewsets,mixins
from .models import *
from .serializers import *

# Create your views here.


class CategoryListFilter(filters.FilterSet):
    category_name = filters.CharFilter(method="filter_by_category_name")

    def filter_by_category_name(self, queryset, name, value):
        if value is None:
            return queryset
        try:

            return queryset.filter(name__contains=value)
        except:
            return queryset.none()


class PublicCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = PublicCategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CategoryListFilter


class TagListFilter(filters.FilterSet):
    tag_name = filters.CharFilter(method="filter_by_tag_name")

    def filter_by_tag_name(self, queryset, name, value):
        if value is None:
            return queryset
        try:

            return queryset.filter(name__contains=value)
        except:
            return queryset.none()


class PublicTagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = PublicTagSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TagListFilter


class PublicCommentViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentPublicSerializer


class PublicReactViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = React.objects.all()
    serializer_class = ReactPublicSerializer


class PostListFilter(filters.FilterSet):
    title = filters.CharFilter(method="filter_by_post_title")
    subtitle = filters.CharFilter(method="filter_by_post_subtitle")
    body = filters.CharFilter(method="filter_by_post_body")

    def filter_by_post_title(self, queryset, name, value):
        if value is None:
            return queryset
        try:

            return queryset.filter(title__contains=value)
        except:
            return queryset.none()

    def filter_by_post_subtitle(self, queryset, name, value):
        if value is None:
            return queryset
        try:

            return queryset.filter(subtitle__contains=value)
        except:
            return queryset.none()

    def filter_by_post_body(self, queryset, name, value):
        if value is None:
            return queryset
        try:

            return queryset.filter(body__contains=value)
        except:
            return queryset.none()


class PublicPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = FlatPostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostListFilter

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by("-id")

    def get_serializer_class(self):
        if self.action == "list":
            return FlatPostSerializer
        return PublicPostSerializer
