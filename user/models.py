from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user_info = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10,default='None')
    
    # password=models.CharField(null=False,max_length=20)
    def __str__(self):
        return str(self.user_info.username)

