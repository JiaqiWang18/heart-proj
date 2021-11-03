# Generated by Django 3.2.9 on 2021-11-03 04:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', ckeditor.fields.RichTextField()),
                ('ECG_image', models.ImageField(blank=True, upload_to='ECGs')),
            ],
        ),
    ]