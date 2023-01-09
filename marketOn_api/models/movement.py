from models import*
from product import *
from inventory import *
from assistant import *
from seller import *
from report import *
class Movement():
     quantity = models.IntegerField()
     stock = models.IntegerField()
     new_left = models.BooleanField(default=True)
     date = models.DateField()
     product= models.ForeignKey(Product, on_delete=models.CASCADE)
     inventory= models.ForeignKey(Inventory, on_delete=models.CASCADE)
     assistant= models.ForeignKey(Assistant, on_delete=models.CASCADE)
     seller= models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True,
        null=True)
     report = models.ManyToManyField(Report)