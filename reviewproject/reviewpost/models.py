from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ReviewModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    useful_num = models.IntegerField(null = True, blank = True, default = 0)
    project_image = models.ImageField(upload_to = '', null =True, blank = True)

