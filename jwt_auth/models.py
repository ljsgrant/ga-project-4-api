from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.CharField(max_length=300, blank=True)
    # photos = models.ManyToManyField('photos.Photo', related_name='photo_owner')

    def __str__(self):
        return f"{self.username}"
