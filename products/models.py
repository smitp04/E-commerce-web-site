from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    pid = models.IntegerField(primary_key=True,default=None)      
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
             return str([self.pid, self.name, self.price, self.stock, self.price])

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

