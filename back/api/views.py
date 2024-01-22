from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from urllib.parse import unquote, quote


@api_view(["GET"])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


# Products
@api_view(["GET"])
def get_product(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'in_stock']


class ProductByID(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']


@api_view(["GET"])
def product_search(request):
    request_str = request.get_full_path_info()
    search = request_str[request_str.index("=")+1:]
    search_encode = unquote(search).lower()
    serializer = ProductSerializer(Product.objects.all(), many=True)
    resp = []
    for od in serializer.data:
        if od["name"].lower().find(search_encode)!=-1:
            resp.append(od)
    return Response(resp)

# End of products


# @api_view(["POST"])
# def additem(request):
#     serializer = ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

