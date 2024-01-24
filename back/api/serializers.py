from rest_framework import serializers
from base.models import Category, Product
from urllib.parse import unquote, quote

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "slug", "name","price", 'photo', "in_stock", "desc", "category",)
