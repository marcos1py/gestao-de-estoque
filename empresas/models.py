from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)  # Defina como True se desejar que o usuário acesse a área de administração
    is_active = models.BooleanField(default=True)  # Defina como True para permitir login
    is_superuser = models.BooleanField(default=False)  # Defina como True para dar acesso total à administração

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
