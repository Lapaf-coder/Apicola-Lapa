from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):

    ROLES = (
        ('Administrador', 'Administrador'),
        ('Apicultor', 'Apicultor'),
        ('Vendedor', 'Vendedor'),
    )

    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default='Apicultor'
    )

    def __str__(self):
        return self.username