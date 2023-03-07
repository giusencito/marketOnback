from django.db import models

from apps.seller.models import Seller
from apps.inventory.models import Inventory
from apps.products.models import Product
from apps.assistant.models import Assistant
from apps.base.models import BaseModel
# Create your models here.
class Movement(BaseModel):
    quantity = models.IntegerField()
    new_left = models.BooleanField(default=True)
    date = models.DateField()
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    inventory= models.ForeignKey(Inventory, on_delete=models.CASCADE)
    assistant= models.ForeignKey(Assistant, on_delete=models.CASCADE)
    seller= models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True,
        null=True)
    
    class Meta:
          verbose_name = 'Movement'
          verbose_name_plural = 'Movements'
    def __str__(self):
           
        return f'{self.id}'