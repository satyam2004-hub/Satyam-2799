from django.db import models
from orders.models import Order

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_id = models.CharField(max_length=100)  
    status = models.CharField(max_length=20)  
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Payment {self.payment_id} for Order #{self.order.pk}"
