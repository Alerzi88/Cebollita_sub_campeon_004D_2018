from django.db import models
# Create your models here.
class Datos(models.Model):
    title = models.CharField(max_length=200)