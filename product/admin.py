from django.contrib import admin
from .models import Product, ProductImage


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ("name", "actual_price", "selling_price")

    class Meta:
        model = Product


@admin.register(ProductImage)
class PostAdmin(admin.ModelAdmin):
    list_display = ("product",)
    class Meta:
        model = ProductImage
