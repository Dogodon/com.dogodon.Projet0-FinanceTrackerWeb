from django.db import models

# Create your models here.

# authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Ajouter des champs personnalisés
    full_name = models.CharField(max_length=100, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username