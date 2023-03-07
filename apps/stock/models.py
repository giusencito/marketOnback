from django.db import models
from apps.base.models import BaseModel
from apps.inventory.models import Inventory
from apps.products.models import Product
# Create your models here.
class Stock(BaseModel):
      stock = models.IntegerField()
      inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
      product = models.ForeignKey(Product, on_delete=models.CASCADE)
      class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'