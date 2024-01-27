from django.contrib import admin
from .models import Category, Product, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}
    list_display = ('name', 'slug')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'in_stock', "price")
    prepopulated_fields = {'slug': ("name",)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'surname', 'email', 'phone', 'basket',)
