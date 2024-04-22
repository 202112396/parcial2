from django.db import models

# Create your models here.
class Usuarios(models.Model):
    user_id = models.CharField(max_length=100)