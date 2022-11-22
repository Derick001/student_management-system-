from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Authentication(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='authentication')
    phone=models.IntegerField( null=False)
    role=models.CharField(max_length=50, null=False)
    
    
    
    
    
    