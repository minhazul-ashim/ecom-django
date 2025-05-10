import os
from uuid import uuid4
from django.db import models

def store_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}{ext}"

    return os.path.join("store", filename)

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
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    description = models.TextField()
    address = models.TextField()
    currency = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    contact_details = models.TextField()
    logo = models.ImageField(upload_to=store_path)
    banner_1 = models.ImageField(upload_to=store_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'StoreInfo'
        verbose_name_plural = 'StoreInfo'
        db_table = 'store_info'

    def __str__(self):
        return f'{self.id} | {self.name}'
    
class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    icon = models.ImageField(upload_to=store_path)
    store_id = models.ForeignKey(StoreInfo, on_delete=models.CASCADE, related_name='social_media')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'SocialMedia'
        verbose_name_plural = 'SocialMedia'
        db_table = 'social_media'

    def __str__(self):
        return f'{self.id} | {self.name}'
    
class ExtraPage(models.Model):
    param_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    page_content = models.TextField()
    store_id = models.ForeignKey(StoreInfo, on_delete=models.CASCADE, related_name='extra_pages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'ExtraPage'
        verbose_name_plural = 'ExtraPages'
        db_table = 'extra_page'

    def __str__(self):
        return f'{self.id} | {self.title}'
    
class StoreGallery(models.Model):
    name = models.CharField(max_length=50)
    store_id = models.ForeignKey(StoreInfo, on_delete=models.CASCADE, related_name='store_galleries')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'StoreGallery'
        verbose_name_plural = 'StoreGalleries'
        db_table = 'store_gallery'

    def __str__(self):
        return f'{self.id} | {self.name}'
    

class StoreUpload(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200)
    image = models.ImageField(upload_to=store_path)
    priority = models.IntegerField(default=1)
    store_gallery_id = models.ForeignKey(StoreGallery, on_delete=models.CASCADE, related_name='store_gallery_uploads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'StoreUpload'
        verbose_name_plural = 'StoreUploads'
        db_table = 'store_upload'

    def __str__(self):
        return f'{self.id} | {self.title}'