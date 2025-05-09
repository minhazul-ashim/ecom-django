from django.db import models

# Create your models here.
class Attribute(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} | {self.name}'
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'
        db_table = 'attribute'

class AttributeItem(models.Model):
    name = models.CharField(max_length=50)
    attr_id = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='attribute_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'AttributeItem',
        verbose_name_plural = 'AttributeItems'
        db_table = 'attribute_item'

    def __str__(self):
        return f'{self.id} | {self.name}'
    
class UnitType(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'UnitType'
        verbose_name_plural = 'UnitTypes'
        db_table = 'unit_type'

    def __str__(self):
        return f'{self.id} | {self.name}'
    
class StoreInfo(models.Model):
    name = models.CharField(max_length=50)