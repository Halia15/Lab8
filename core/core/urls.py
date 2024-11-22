from django.contrib import admin
from django.urls import path

from projects import views

urlpatterns = [
    path("admin/",admin.site.urls),
    path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('products/', views.product_list, name='product_list'),
    path('clients/', views.client_list, name='client_list'),
    path('sales/', views.sale_list, name='sale_list'),
    path("", views.index),
]
