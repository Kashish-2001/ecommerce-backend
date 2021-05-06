from django.db import models
from django.db.models.signals import pre_save
from ecommerce.utils import unique_slug_generator


class Product(models.Model):
    CATEGORIES_CHOICES = [
        ('Women', 'Women'),
        ('Men', 'Men'),
        ('Unisex', 'Unisex'),
        # ('Kids', 'Kids'),
    ]

    SUB_CATEGORIES_CHOICES = [
        ('T-shirt', 'T-shirt'),
        ('Shirt', 'Shirt'),
        ('Jeans', 'Jeans'),
        ('Accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=200)
    actual_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField(null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORIES_CHOICES,
    )
    sub_category = models.CharField(
        max_length=50,
        choices=SUB_CATEGORIES_CHOICES,
    )

    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/', default=None, max_length=500)
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


# Default selling price
def default_selling_price(sender, instance, *args, **kwargs):
    if not instance.selling_price:
        instance.selling_price = instance.actual_price


pre_save.connect(default_selling_price, sender=Product)


# Slug Generator
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Product)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, related_name="image")
    images = models.ImageField(upload_to='product_images/', max_length=500)

    def __str__(self):
        return self.product.name

