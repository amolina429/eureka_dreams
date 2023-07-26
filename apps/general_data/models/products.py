from django.db import models
from .subcategories import Subcategories

# Create your models here.

class Products(models.Model):
        product_id = models.PositiveIntegerField('Product Id', blank=False, null=False)
        id_third_parties = models.CharField('Identificación del Tercero', max_length=100, primary_key=True, unique=True)
        subcategory_id = models.ForeignKey(Subcategories, on_delete=models.CASCADE, db_column="subcategory_id", null=False, blank=False)
    
        class Meta:
            db_table = 'products'
            verbose_name = 'product'
            verbose_name_plural = 'products'

