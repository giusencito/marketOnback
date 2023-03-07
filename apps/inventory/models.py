from django.db import models
from apps.base.models import BaseModel
# Create your models here.
from apps.office.models import Office

class Inventory(BaseModel):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    class Meta:
          verbose_name = 'Inventory'
          verbose_name_plural = 'Inventories'
    
    def __str__(self):
           
        return f'{self.id} with {self.quantity}'