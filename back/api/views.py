from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from urllib.parse import unquote, quote
from django.core.mail import send_mail
from django.conf import settings


def email_message_former(data):
    """
    Forms the email from given data in basket
 
    Args:
        data (dict): basket
 
    Returns:
        str: formed email
    """
    try:
        product_string = ""
        total = 0
        for product in data['basket']:
            product_string += f"{float(product['price']) * int(product['amount'])}грн  {product['name']} X{product['amount']}\n        "
            total += float(product['price']) * product['amount']

        message = f"""Замовлення на ім'я {data['name']} {data['surname']}\n
        {product_string}\n Всього до оплати: {total}грн"""
        return message
    except:
        return ValueError


@api_view(["POST"])
def order(request):
    """
    Creates order

    """
    try:
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        send_mail("Order Confirmation", email_message_former(serializer.data), settings.EMAIL_HOST_USER,
                [serializer.data["email"]])
        return Response(serializer.data)
    except:
            return ValueError


@api_view(["GET"])
def get_categories(request):
    """
    Forms json of categories

    """
    try:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    except:
            return ValueError


@api_view(["GET"])
def get_product(request, pk):
    """
    Forms json of product by id given as pk

    """
    try:
        products = Product.objects.get(id=pk)
        serializer = ProductSerializer(products, many=False)
        return Response(serializer.data)
    except:
            return ValueError


class ProductList(generics.ListAPIView):
    """
    Displays all the products

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'in_stock']

#Нижче так багато коду тому що SearchFilter з DRF Є CASESENSITIVE для кірилиці SqLite3
@api_view(["GET"])
def product_search(request):
    """
    Search for Products by category and in_stock status

    """
    try:
        request_str = request.get_full_path_info()
        search = request_str[request_str.index("=") + 1:]
        search_encode = unquote(search).lower()
        serializer = ProductSerializer(Product.objects.all(), many=True)
        resp = []
        for od in serializer.data:
            if od["name"].lower().find(search_encode) != -1:
                resp.append(od)
        return Response(resp)
    except:
            return ValueError
