from django.db import models
from category.models import Category
from subcategory.models import Subcategory
from django import db

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # stock = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='subcategory_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Product'
        ordering = ['-id']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
