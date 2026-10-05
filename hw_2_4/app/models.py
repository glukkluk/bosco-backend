from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    age_category = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
