# Generated by Django 3.2.9 on 2021-11-10 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0004_alter_disease_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='updated_at',
        ),
    ]