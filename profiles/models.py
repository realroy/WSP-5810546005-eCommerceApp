from django.db import models


# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='description default text')
    location = models.CharField(max_length=120, default='location', blank=True, null=True)
    job = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.name
