from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('products/', ProductList.as_view(), name="products"),
    # path('products/<int:product_id>/', ProductDetail.as_view(), name="product"),
    path('products/<slug:slug_text>/', ProductDetail.as_view(), name="product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)