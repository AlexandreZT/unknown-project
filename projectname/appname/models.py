from django.db import models

# Create your models here.
class appname(models.Model):
    image = models.ImageField(upload_to='../projectname/static/media/images/')
    summary = models.CharField(max_length=200)