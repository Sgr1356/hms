from django.db import models


# Create your models here.
class docpatmodel(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    emailid = models.EmailField(max_length=50)
    contact = models.IntegerField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)


class loginmodel(models.Model):
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
