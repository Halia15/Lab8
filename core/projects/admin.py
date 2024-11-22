from django.contrib import admin
from .models import Warehouse, Client, Product, Sale
admin.site.register(Client)
admin.site.register(Warehouse)
admin.site.register(Product)
admin.site.register(Sale)
