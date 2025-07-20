from django.db import models
from users.models import Users

class Booking(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateTimeField(null=True, blank=True)  # set when booking ends
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Confirmed', 'Confirmed'),
            ('Cancelled', 'Cancelled')
        ],
        default='Pending'
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking {self.id} - User {self.user.name}"



   
