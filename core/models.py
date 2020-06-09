from django.db import models

# Create your models h


class Category(models.Model):
    category_name = models.CharField(max_length=80)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=80)
    def __str__(self):
        return self.product_name