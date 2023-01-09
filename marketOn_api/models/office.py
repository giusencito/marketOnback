from models import *
from boss import *
class Office():
    name = models.CharField(max_length=30)
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE)