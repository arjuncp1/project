from django.db import models


# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()


