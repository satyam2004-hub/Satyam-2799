from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.

class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_date=models.DateTimeField(auto_now_add=True)
    payment_method=models.CharField(max_length=50,choices=[
        ('Credit Card','Credit Card'),
        ('Cash','Cash'),
        ('Paypal','Paypal')
    ])

    status = models.CharField(max_length=20, choices=[
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
    ('Failed', 'Failed')
], default='Pending')



    def __str__(self):
        return f"{self.user.username}-{self.product.name}-{self.amount}"
