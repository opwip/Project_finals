from django.urls import path
from . import views

urlpatterns = [
    path('', views.getdata),
    path('add/', views.additem),
    path('search/', views.ProductList.as_view()),
    path('list/', views.UserListView.as_view())
]
