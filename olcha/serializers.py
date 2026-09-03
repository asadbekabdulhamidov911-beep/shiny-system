from rest_framework import serializers
from .models import Swiper1, Swiper2, Product, Category

class Swiper1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Swiper1
        fields = ['id', 'image']

class Swiper2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Swiper2
        fields = ['id', 'image', 'name', 'price']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'price']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'image', 'name']