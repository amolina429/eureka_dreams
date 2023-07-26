from django.db import models

# Create your models here.

class Categories(models.Model):
        id = models.BigAutoField('Category Id', primary_key=True)
        nombre = models.CharField('Category Name', blank=False, max_length=100, null=False)
    
        class Meta:
            db_table = 'categories'
            verbose_name = 'category'
            verbose_name_plural = 'categories'

