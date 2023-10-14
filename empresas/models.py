from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Change to a list

    def __str__(self):
        return self.username


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=300)
    bio=models.CharField(max_length=300)
    image=models.ImageField(default="default.jpg",upload_to="user_images")
    verified=models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


# Abstract user: Customizing authentication in Django
# The authentication that comes with Django is good enough for most common cases, 
# but you may have needs not met by the out-of-the-box defaults. 
# Customizing authentication in your projects requires understanding what points of the provided system are extensible or replaceable. 