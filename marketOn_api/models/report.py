from django.db import models
from assistant import *

class Report():
    description= models.CharField(max_length=100)
    start = models.DateField()
    finish = models.DateField()
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE)
    