from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Product, ProductType
from .serializer import ProductSerializer, ProductTypeSerializer, UserSerializer


# Create your views here.
class UserRegister(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    
    permission_classes = [IsAuthenticated]

    def get_obj(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        product = self.get_obj(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        product = self.get_obj(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        product = self.get_obj(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductTypeList(APIView):
   
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        product_type = ProductType.objects.all()
        serializer = ProductTypeSerializer(product_type, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        product_type_serializer = ProductTypeSerializer(data=request.data)
        if product_type_serializer.is_valid():
            product_type_serializer.save()
            return Response(product_type_serializer.data, status=status.HTTP_201_CREATED)
        return Response(product_type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    