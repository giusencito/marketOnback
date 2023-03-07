from django.db import models
from apps.boss.models import Boss
from apps.base.models import BaseModel
# Create your models here.
class Office(BaseModel):
    name = models.CharField(max_length=30)
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE)
    class Meta:
          verbose_name = 'office'
          verbose_name_plural = 'offices'
    def __str__(self):
           
        return self.name