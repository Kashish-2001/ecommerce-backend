from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name="products"),
    # path('products/<int:product_id>/', ProductDetail.as_view(), name="product"),
    path('products/<slug:slug_text>/', ProductDetail.as_view(), name="product"),
]

