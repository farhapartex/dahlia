from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.


class PublicProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = PublicProfileSerializer

    def get_queryset(self):
        try:
            user = User.objects.get(is_superuser=True)
            return Profile.objects.filter(user=user)
        except :
            return []


