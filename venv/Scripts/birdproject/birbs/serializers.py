from rest_framework import serializers
from .models import BirdSighting

class BirdSightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdSighting
        fields = ['id', 'species', 'location', 'date_seen', 'picture']