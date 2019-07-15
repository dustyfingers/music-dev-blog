from django.db import models
from datetime import datetime
from authors.models import Author


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
