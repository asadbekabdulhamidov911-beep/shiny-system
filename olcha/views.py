from django.shortcuts import render
from rest_framework import viewsets

from .models import Swiper1, Swiper2, Product, Category
from .serializers import Swiper1Serializer, Swiper2Serializer, ProductSerializer, CategorySerializer

class Swiper1ViewSet(viewsets.ModelViewSet):
    queryset = Swiper1.objects.all()
    serializer_class = Swiper1Serializer

class Swiper2ViewSet(viewsets.ModelViewSet):
    queryset = Swiper2.objects.all()
    serializer_class = Swiper2Serializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def index(request):
    return render(request, 'index.html')