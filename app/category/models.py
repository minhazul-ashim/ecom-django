from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    thumb = models.ImageField(upload_to='categories/', blank=True, null=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = 'Category'
        db_table = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.id} - {self.name}'