# Generated by Django 3.1.7 on 2021-03-12 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyPressApp', '0003_pypress_pages_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='pypress_pages',
            name='footer',
            field=models.TextField(default='x'),
            preserve_default=False,
        ),
    ]
