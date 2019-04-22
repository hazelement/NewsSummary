from django.db import models
from datetime import datetime
# Create your models here.


class UrlDigestionDBModel(models.Model):

    url = models.TextField(primary_key=True)
    digestion = models.TextField(default="")
    author = models.TextField(default="")
    title = models.TextField(default="")
    publish_date = models.TextField(default="")

    update_time = models.DateTimeField(default=datetime.utcnow)
