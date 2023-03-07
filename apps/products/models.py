from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
# Create your models here.
class Category(BaseModel):
     name = models.CharField(max_length=30,unique=True,blank=False)
     description = models.CharField(max_length=100)
    
     class Meta:
          verbose_name = 'category'
          verbose_name_plural = 'categories'
     def __str__(self):
           
        return self.name
    
    
class Product(BaseModel):
     name = models.CharField(max_length=30)
     description = models.CharField(max_length=100)
     price = models.FloatField()
     category= models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name = 'category')
     image=models.ImageField('ProductImage', upload_to='products/',blank=True,null=True)
    
    
     class Meta:
          verbose_name = 'product'
          verbose_name_plural = 'products'
     def __str__(self):
           
        return self.name

