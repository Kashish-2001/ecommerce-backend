from django.db import models
from django.db.models.signals import pre_save
from ecommerce.utils import unique_slug_generator


class Product(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]
    name = models.CharField(max_length=200) # unique or not??
    price = models.PositiveIntegerField()
    size = models.CharField(
        max_length=2,
        choices=SIZE_CHOICES,
        default="S",
    )
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/', default=None)
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, related_name="images")
    images = models.FileField(upload_to='product_images/')

    def __str__(self):
        return self.product.name


# Slug Generator

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Product)