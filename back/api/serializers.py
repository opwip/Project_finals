from rest_framework import serializers
from base.models import Category, Product, Order
from urllib.parse import unquote, quote


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "slug", "name", "price", 'photo', "in_stock", "desc", "category",)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
