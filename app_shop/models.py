from django.db import models

# Create your models here.
class Product(models.Model):
    price = models.IntegerField()
    image = models.CharField(max_length=500)
    description = models.CharField(max_length=800)
    quantity = models.IntegerField()

