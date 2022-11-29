from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name=models.CharField(max_length=250,null=False)
    last_name=models.CharField(max_length=250,null=False)
    other_name=models.CharField(max_length=250,null=False)
    address=models.CharField(max_length=250, null=False)
    d_o_b=models.DateField(auto_now_add=False, auto_now=False)
