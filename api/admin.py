from django.contrib import admin

# Register your models here.
from .models import Location, Item
admin.site.register(Item)
admin.site.register(Location)
