from django.db import models
from category.models import Category

# Create your models here.
class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    thumb = models.ImageField(upload_to='subcategories/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        db_table = 'subcategory'
        verbose_name='Subcategory'
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return f'{self.id} | {self.name}'