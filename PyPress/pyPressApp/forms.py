from django import forms
from django_ckeditor_5.fields import CKEditor5Field

class PyPress_Edit_Pages(forms.Form):
    name = forms.CharField(max_length=300)
    post = CKEditor5Field('Text', config_name='extends')
    slug = forms.CharField(max_length=300)