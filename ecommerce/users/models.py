from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10, unique=True)
    # username = None

    # USERNAME_FIELD = 'phone'