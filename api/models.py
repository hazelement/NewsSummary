from django.db import models
from datetime import datetime
# Create your models here.


class UrlDigestion(models.Model):

    url_hash = models.TextField(primary_key=True)
    url = models.TextField(default="")
    url_digestion = models.TextField(default="")
    update_time = models.DateTimeField(default=datetime.utcnow)
