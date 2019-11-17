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

class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
