from orders.placeorder import place_order
from django.urls import  path

urlpatterns = [
    path('placeorder', place_order),


]