from django.contrib import admin
from .models import Category, Product, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}
    list_display = ('name', 'slug')
    list_filter = ["id", 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'in_stock', "price")
    prepopulated_fields = {'slug': ("name",)}
    list_filter = ["id", 'name', 'in_stock']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'surname', 'email', 'phone', 'basket',)
    list_filter = ["id", 'name']


@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", 'photo', 'amount')
    list_filter = ["id", 'name']