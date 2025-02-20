from django.urls import path
from .views import ProductList, ProductTypeList, ProductDetail


urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('products-type/', ProductTypeList.as_view(), name='products-type'),
]