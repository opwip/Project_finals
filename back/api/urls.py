from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.product_search),
    path("categories", views.get_categories),
    path('products/', views.ProductList.as_view()),
    path('product/<str:pk>', views.get_product),
]
