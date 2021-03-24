# Generated by Django 3.1.7 on 2021-03-23 06:44

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pyPressApp', '0008_auto_20210320_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HomePage', django_ckeditor_5.fields.CKEditor5Field(verbose_name='HTML')),
            ],
        ),
        migrations.CreateModel(
            name='ThemeVariables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VariableName', models.CharField(max_length=200)),
                ('VariableData', models.CharField(max_length=500)),
            ],
        ),
    ]
