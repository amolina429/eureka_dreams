from django.db import models
from .categories import Categories

# Create your models here.

class Subcategories(models.Model):
        id = models.BigAutoField('Sub Category Id', primary_key=True)
        category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, db_column="category_id", null=False, blank=False)
        description = models.CharField('Subcategory Description', blank=False, max_length=100, null=False, default='')
    
        class Meta:
            db_table = 'subcategories'
            verbose_name = 'subcategory'
            verbose_name_plural = 'subcategories'

