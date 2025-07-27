from django.db import models

CATEGORY = (('hobby', '趣味'),('study', '勉強'), ('other', 'その他'))
# Create your models here.
class FirstModel(models.Model):
    title = models.CharField(max_length = 100)
    number = models.IntegerField()


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length = 100,
        choices = CATEGORY
    )
    def __str__(self):
        return self.title