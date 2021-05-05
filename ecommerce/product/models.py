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
    images = models.ImageField(upload_to='static')
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Product)