from .models import Product, ProductImage
from rest_framework import serializers


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('images',)


class ProductSerializer(serializers.ModelSerializer):
    image = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ("name", 'selling_price', "actual_price", 'category', 'sub_category', "brand", "description",  'thumbnail', 'slug', "image", )