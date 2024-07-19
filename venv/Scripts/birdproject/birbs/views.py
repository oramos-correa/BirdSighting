from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import BirdSighting
from .serializers import BirdSightingSerializer

class BirdSightingViewSet(viewsets.ModelViewSet):
    queryset = BirdSighting.objects.all()
    serializer_class = BirdSightingSerializer

# New view for the root URL
def index(request):
    return HttpResponse("Welcome to the BirdSightings API")
