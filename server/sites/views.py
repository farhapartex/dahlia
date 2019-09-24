from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *

# Create your views here.

"""
API Views
"""


class PublicSiteAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = SiteInformation.objects.all()
    serializer_class = PublicSiteInformationSerializer

    # def get_queryset(self):
    #     return MenuItem.objects.filter(parent_menu=None)
