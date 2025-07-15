from asyncio.base_futures import _PENDING
from django.db import models

# Create your models here.

class order(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_name=models.CharField(max_length=100)
    user_id=models.IntegerField()
    placed_at=models.DateTimeField(auto_now_add=True)

    PAYMENT_STATUS_CHOICE =[
        ('PENDING','pending')
        ('FAILED','failed')
        ('PAID','paid')
        ('REFUNDED','refunded')
    ]
    payment_status=models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICE,
        default='PENDING'
    )
    def _str_(self):
        return f"Order{self.order_id} by User {self.user_id}"

   
