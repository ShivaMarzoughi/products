from django.urls import path
from .views import product_list,product_items
urlpatterns = [
    path('product_list/', product_list, name='product-list'),
    path('product/<slug:slug>/', product_items, name='product-item'),
]
