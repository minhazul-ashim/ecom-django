from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    thumb = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = 'Category'
        db_table = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.id} - {self.name}'