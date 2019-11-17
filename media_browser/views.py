from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .permissions import *
# Create your views here.

class MediaImagePrivateAPIView(viewsets.ModelViewSet):
    queryset = MediaImage.objects.all()
    serializer_class = MediaImagePrivateSerializer
    permission_classes = (IsAuthenticated,IsAdminOrReadOnly,)
