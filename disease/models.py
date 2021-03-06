from django.db import models

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=30)
    tags = TaggableManager()
    short_description = models.CharField(max_length=60)
    description = RichTextField()
    ECG_image = models.ImageField(upload_to='ECGs', blank=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name