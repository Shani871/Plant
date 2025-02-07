from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.title
    title= models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=300)


class Order(models.Model):
    def __str__(self):
        return self.name
    item = models.CharField(max_length=1000)
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    total = models.CharField(max_length=200)