from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('stocks/', views.stocks, name='stocks'),
    path('add_stock/', views.add_stock,name='add_stock'),
    path('sales/', views.sales,name='sales'),
    path('edit_stock/<int:id>/', views.edit_stock, name='edit_stock'),
    path('stock_check/', views.stock_check, name='stock_check'),
]
