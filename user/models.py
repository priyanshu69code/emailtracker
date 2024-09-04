from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile = models.ImageField(upload_to='profile/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> Any:
        return self.email
