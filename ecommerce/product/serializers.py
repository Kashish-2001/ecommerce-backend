from .models import Product, ProductImage
from rest_framework import serializers


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('images',)


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ("images", "name", 'price', 'size', 'thumbnail', 'slug' )

