# urls.py
from django.urls import path
from .views import product_list,get_products, add_product, update_category,board_page

urlpatterns = [
    path("", product_list, name="product_list"),
    path('products', get_products),
    path('products/add', add_product),
    path('products/<str:barcode>', update_category),
    path('board/', board_page),
]
