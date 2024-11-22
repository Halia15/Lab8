# views.py

from django.shortcuts import render
from .models import Warehouse, Product, Client, Sale

# View для виведення всіх складів
def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'warehouses.html', {'warehouses': warehouses})

# View для виведення всіх товарів
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

# View для виведення всіх клієнтів
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

# View для виведення всіх продажів
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales.html', {'sales': sales})

def index(request):
    return render(request, "index.html")
