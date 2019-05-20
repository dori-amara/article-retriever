from django.db import models
from django.utils import timezone


class Article(models.Model):
    date_retrieved = models.DateTimeField(default=timezone.now)
    source_id = models.CharField(max_length=256)
    date_published = models.CharField(max_length=20)
    author = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=512)
    content = models.TextField()
