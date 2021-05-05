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
        fields = ("name", 'selling_price', "actual_price", 'size', 'thumbnail', 'slug', "images")