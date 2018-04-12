from django.db import models
from django.conf import settings

# Create your models here.


class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='description default text')

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return self.name
