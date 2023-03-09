from django.urls import path
from .views import ItemList, ItemDetail, LocationList, LocationDetail

urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
]
#http://127.0.0.1:8000/api/item/
#http://127.0.0.1:8000/api/location/