from models import *
from category import *
class Product():
     name = models.CharField(max_length=30)
     description = models.CharField(max_length=100)
     price = models.FloatField()
     category= models.ForeignKey(Category, on_delete=models.CASCADE)