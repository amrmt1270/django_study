from django.contrib.auth.models import AbstractUser
from django.db import models 


# Create your models here.
class Account(AbstractUser):
    avator = models.ImageField(
        upload_to = '',
        null = True,
        blank = True
    )

