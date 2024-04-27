from distutils.command.upload import upload
from django.db import models

# Create your models here.

class recipies(models.Model):
    recipies_name = models.CharField(max_length=500)
    description = models.TextField()
    recipie_image = models.ImageField(upload_to='veg/static')
