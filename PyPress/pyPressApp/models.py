from django.db import models
# Create your models here.
class PyPress_Pages(models.Model):
    name = models.CharField(max_length=300)
    head = models.TextField()
    body = models.TextField()
    footer = models.TextField()
    slug = models.CharField(max_length=300)

from django_ckeditor_5.fields import CKEditor5Field


class Article(models.Model):
    title=models.CharField('Title', max_length=200)
    text=CKEditor5Field('Text', config_name='extends')