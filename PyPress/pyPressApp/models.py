from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class PyPress_Pages(models.Model):
    name = models.CharField(max_length=300)
    post=CKEditor5Field('Text', config_name='extends')
    slug = models.CharField(max_length=300)




class Settings(models.Model):
    DefaultPage=models.CharField('DeafualtPage', max_length=200)

class ThemeDesign(models.Model):
    HomePage = models.TextField()

class ThemeVariables(models.Model):
    VariableName = models.CharField(max_length=200)
    VariableData = models.CharField(max_length=500)