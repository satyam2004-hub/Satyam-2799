from django.db import models

# Create your models here.

class Order(models.Model):
    user_id=models.IntegerField()
    start_date=models.DateField()
    rental_item_id=models.IntegerField()
    end_date=models.DateField()
    total_price=models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"Order {self:id} for users {self:user_id}"
    

    
