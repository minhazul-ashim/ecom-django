from django.db import models
from category.models import Category
from subcategory.models import Subcategory

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='subcategory_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.id} - {self.name}'


class ProductVariant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=False, blank=False, default=0, )
    image = models.ImageField(upload_to='products/variants/', null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_variants')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'productvariant'
        ordering = ['-id']
        verbose_name = 'ProductVariant'
        verbose_name_plural = 'ProductVariants'

    def __str__(self):
        return f'{self.id} - {self.name}'

class PriceVariant(models.Model):
    description = models.TextField()
    min_qty = models.IntegerField(null=False, blank=False, default=0)
    max_qty = models.IntegerField(null=False, blank=False, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_variant_id = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='product_variant_prices', null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_prices', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='pricevariant'
        ordering = ['-id']
        verbose_name = 'PriceVariant'
        verbose_name_plural = 'PriceVariants'

    def __str__(self):
        return f'{self.id} - {self.description}'