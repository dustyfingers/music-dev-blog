from django.db import models
from datetime import datetime


class Author(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.CharField(max_length=200)
    joined_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
