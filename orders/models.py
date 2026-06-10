from django.db import models

# Create your models here.

class orders(models.Model):
    order_number = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_number