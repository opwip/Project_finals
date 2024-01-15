from django.contrib import admin
from .models import Item, Category, Product


# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}
    list_display = ('name', 'slug')


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ("name",)}
#     list_display = ('name', 'in_stock', "price")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'in_stock', "price")
    prepopulated_fields = {'slug': ("name",)}
    