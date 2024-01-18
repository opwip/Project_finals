from django.urls import path
from . import views

urlpatterns = [
    path('', views.getdata),
    path('add/', views.additem),
    path('search/', views.ProductSearch.as_view()),
    path('list/', views.UserListView.as_view()),
    path('test/<str:pk>', views.getdata_from_categories),
    path("categories", views.get_categories),
    path('products/', views.ProductList.as_view()),   
]
