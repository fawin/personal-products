from django.db import models

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(null=False, blank=False)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)