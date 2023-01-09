from models import *
from office import *
class Inventory():
    office = models.ForeignKey(Office, on_delete=models.CASCADE)