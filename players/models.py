from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to="profiles/", default="steve.png")
