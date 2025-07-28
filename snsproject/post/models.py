from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'post_owner'
    )
    content = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

