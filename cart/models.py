from django.db import models
from products import models as pm
from django.contrib.auth.models import User

class Cart(models.Model):
    username = models.CharField(max_length=50)
    productkey = models.IntegerField()
    productname = models.CharField(max_length=80,default=None)
    image_url = models.CharField(max_length=4088, default=None)
    quantity = models.IntegerField(null=False,default=0)
    total_price  = models.FloatField(null=False,default=0)  
    
    def __str__(self):
        return self.username     
       
    
       
