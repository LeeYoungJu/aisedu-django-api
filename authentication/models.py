from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    url = models.CharField(max_length=100, null=True)
