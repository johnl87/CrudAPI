from rest_framework import generics

from .models import Item, Location
from .serializers import ItemSerializer, LocationSerializer

class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        #querys all the data and then will filter using if statement
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            #fliters itemLocation from models.py
            queryset = queryset.filter(itemLocation=location)
        return queryset
    
    #create, read, update, delete - CRUD
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
