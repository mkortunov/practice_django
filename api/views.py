from django.shortcuts import render

from rest_framework import generics, permissions
from .models import *
from .serializers import *

class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ActorSerializer

class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ActorSerializer