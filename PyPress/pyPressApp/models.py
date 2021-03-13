from django.db import models

# Create your models here.
class PyPress_Pages(models.Model):
    name = models.CharField(max_length=300)
    head = models.TextField()
    body = models.TextField()
    footer = models.TextField()
    