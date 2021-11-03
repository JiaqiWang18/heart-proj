from django.db import models

from ckeditor.fields import RichTextField


# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=60)
    description = RichTextField()
    ECG_image = models.ImageField(upload_to='ECGs', blank=True)

    def __str__(self):
        return self.name