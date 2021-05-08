from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10, unique=True, blank=False)
    name = models.CharField(max_length=50, unique=False, blank=False)

    def __Str__(self):
        return self.name + self.phone


# Default username
def default_username(sender, instance, *args, **kwargs):
    if not instance.username:
        instance.username = f'{instance.name}_{instance.phone}'


pre_save.connect(default_username, sender=CustomUser)
