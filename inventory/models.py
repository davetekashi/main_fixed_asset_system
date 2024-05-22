from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    STATUS_CHOICES = [
        ('in_stock', 'In Stock'),
        ('in_use', 'In Use'),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='in_stock')
    date_of_purchase = models.DateField(null=True, default=datetime.date.today)

    def __str__(self):
        return self.name
