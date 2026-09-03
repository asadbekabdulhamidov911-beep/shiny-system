from django.db import models

class Swiper1(models.Model):
    image = models.ImageField(upload_to='swiper1/')

    def __str__(self):
        return f"Swiper1 {self.id}"

class Swiper2(models.Model):
    image = models.ImageField(upload_to='swiper2/')
    name = models.CharField(max_length=100, default='')
    price = models.IntegerField()

    def __str__(self):
        return self.name or f"Swiper2 {self.id}"

class Product(models.Model):
    image = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Category(models.Model):
    image = models.ImageField(upload_to='category/')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 