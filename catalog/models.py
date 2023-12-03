from django.db import models

# Create your models here.
class Catalog(models.Model):
    nombre = models.CharField(max_length=30)
