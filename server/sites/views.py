from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from .models import *
from .serializers import *

# Create your views here.

"""
API Views
"""
class PublicSiteAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = SiteInformation.objects.all()
    serializer_class = PublicSiteInformationSerializer

class ContactCreateAPIView(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

