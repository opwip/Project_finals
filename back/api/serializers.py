from rest_framework import serializers
from base.models import Item, Category, Product


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = Product
        fields = ("id", "slug", "name", "price", 'photo', "in_stock", "desc", "category",)

    def get_photo_url(self, obj):
        return "http://127.0.0.1:8000/" + obj.photo.url
