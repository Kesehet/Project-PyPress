# Generated by Django 3.1.7 on 2021-03-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyPressApp', '0004_pypress_pages_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='pypress_pages',
            name='slug',
            field=models.CharField(default='a', max_length=300),
            preserve_default=False,
        ),
    ]