from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class PyPress_Pages(models.Model):
    name = models.CharField(max_length=300)
    post=CKEditor5Field('Text', config_name='extends')
    slug = models.CharField(max_length=300)




class Article(models.Model):
    title=models.CharField('Title', max_length=200)
    