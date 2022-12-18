from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=64)
    image = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()


    def __str__(self):
        return f"{self.id}: {self.title} -> {self.description}"

# Create your models here.
