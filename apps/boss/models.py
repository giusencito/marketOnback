from django.db import models
from apps.users.models import User
# Create your models here.
class Boss(User):
    class Meta:
        verbose_name = 'Boss'
        verbose_name_plural = 'Bosses'
    user_ptr = models.OneToOneField(User,
        on_delete=models.CASCADE,
        parent_link=True,primary_key=True,
    )
    def __str__(self):
        return f'Boss {self.name} {self.last_name}'
    
 