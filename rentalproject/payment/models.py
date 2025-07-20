from django.db import models
from booking.models import Booking

# Create your models here.
class Payment(models.Model):
    booking=models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_date=models.DateTimeField(auto_now_add=True)
    method=models.CharField(max_length=20, choices=[
        ('Credit Card','credit card'),
        ('Debit Card','debit card'),
        ('Cash','cash'),
        ('Online','on;ine'),
    ])
    status=models.CharField(max_length=20,choices=[
        ('Pending','pending'),
        ('Failed','failed'),
        ('Completed','completed'),
    ],default='pending')

    def __str__(self):
        return f"payment{self.id} for Booking {self.booking.id}"
    