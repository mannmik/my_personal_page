from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 50)
    date = models.DateTimeField(default = timezone.now)
    body = models.TextField()
