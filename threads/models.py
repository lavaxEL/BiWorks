from django.db import models

# Create your models here.
class Thread(models.Model):
    name = models.TextField(unique=True)
