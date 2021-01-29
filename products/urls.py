from django.urls import path
from products.getproducts import get_products
from products.add_product import add_product

urlpatterns = [
    path('getproducts',get_products),
    path('add_product',add_product)
    
]