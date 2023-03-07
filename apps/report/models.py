from django.db import models
from apps.assistant.models import Assistant
from apps.inventory.models import Inventory
from apps.movement.models import Movement
from apps.base.models import BaseModel
# Create your models here.
class Report(BaseModel):
    description= models.CharField(max_length=100)
    start = models.DateField()
    finish = models.DateField()
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    movement = models.ManyToManyField(Movement,blank=True,null=True)
    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'