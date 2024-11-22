
from django.db import models

class Warehouse(models.Model):
    address = models.TextField()
    manager = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.address

class Product(models.Model):
    TYPES = [('женский', 'Жіночий'), ('мужской', 'Чоловічий'), ('детский', 'Дитячий')]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPES)
    manufacturer = models.CharField(max_length=255)
    warehouse = models.ForeignKey(Warehouse, related_name='products', on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sale(models.Model):
    sale_date = models.DateField()
    client = models.ForeignKey(Client, related_name='sales', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='sales', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Sale {self.id}"
