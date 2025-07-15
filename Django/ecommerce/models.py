from django.db import models

# Create your models here.
class users(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=15,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    birth_date=models.DateField(null=True)


class products(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    inventory=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now=True)



