from rest_framework import serializers
from .models import Item, Location
# 1:1 model to serializers. can have more than one serializer per model

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')
        