from django.db import models
from datetime import datetime
# Create your models here.


class UrlDigestionDBModel(models.Model):

    url = models.URLField(primary_key=True)
    digestion = models.TextField(default="")
    author = models.TextField(default="")
    title = models.TextField(default="")
    publish_date = models.TextField(default="")

    update_time = models.DateTimeField(default=datetime.utcnow)


class Site(models.Model):
    name = models.TextField()
    url = models.URLField(primary_key=True)
    description = models.TextField(default="")


class DailyDigestion(models.Model):
    class Meta:
        unique_together = ('site', 'url_digestion',)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    url_digestion = models.ForeignKey(UrlDigestionDBModel, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.utcnow)
