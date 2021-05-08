from django.contrib import admin
from .models import Product, ProductImage, Category, SubCategory


class ProductImageInline(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ("name", "actual_price", "selling_price")

    class Meta:
        model = Product


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product",)
    class Meta:
        model = ProductImage



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

    class Meta:
        model = Category


@admin.register(SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

    class Meta:
        model = SubCategory
