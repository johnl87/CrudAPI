from django.db import models

# Create your models here.
class Location(models.Model):
    locationName = models.CharField(max_length=100, unique=True)

    #provides name instead of ID
    def __str__(self):
        return self.locationName
    
class Item(models.Model):
    itemName = models.CharField(max_length=100)
    date_installed = models.DateField(auto_now_add=True)
    #when model is deleted, all the items at that location is deleted
    itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)

    #string representation of item
    def __str__(self):
        return self.itemName