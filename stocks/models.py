from django.db import models

# Create your models here.
class LiquorStock(models.Model):
    liquor_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    quantity_price = models.DecimalField(max_digits=12, decimal_places=2,default=0)

    def __str__(self):
        return self.liquor_name

class Sale(models.Model):
    liquor_name = models.CharField(max_length=255)
    stock_sold = models.PositiveIntegerField()
    quantity_price = models.DecimalField(max_digits=12, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.liquor_name} - {self.time}"

