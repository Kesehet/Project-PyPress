# Generated by Django 3.1.7 on 2021-03-23 08:10

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pyPressApp', '0009_themedesign_themevariables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themedesign',
            name='HomePage',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]
