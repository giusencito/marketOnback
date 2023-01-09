from models import *
class Category():
     name = models.CharField(max_length=30)
     description = models.CharField(max_length=100)