from django.urls import path
from .views import ProductList, ProductTypeList


urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('products-type/', ProductTypeList.as_view(), name='products-type'),
]