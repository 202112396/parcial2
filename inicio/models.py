from django.db import models

# Create your models here.
class Usuarios(models.Model):
    user_id = models.CharField(max_length=15,null=True,unique=True)
    firstName = models.CharField(max_length=50,null=True)
    lastName = models.CharField(max_length=50,null=True)
    dpi = models.CharField(max_length=13,null=True)
    age = models.DateField(auto_now=False,auto_now_add=False,null=True)
    tel = models.CharField(null=True,blank=True)
    email = models.EmailField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)