from .models import Product, ProductImage, Category, SubCategory
from rest_framework import serializers


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("images",)


class ProductSerializer(serializers.ModelSerializer):
    image = ProductImageSerializer(many=True)
    category = CategorySerializer(many=True)
    subcategory = SubCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "name",
            "brand",
            "selling_price",
            "actual_price",
            "category",
            "subcategory",
            "description",
            "thumbnail",
            "slug",
            "image",
        )
