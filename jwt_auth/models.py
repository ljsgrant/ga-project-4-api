from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    # posts = models.ManyToManyField('posts.Post', related_name='post_owner')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=300)
    # photos = models.ManyToManyField('photos.Photo', related_name='photo_owner')

    def __str__(self):
        return f"{self.username}"