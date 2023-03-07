from django.db import models
from apps.users.models import User
from apps.boss.models import Boss
# Create your models here.

class Assistant(User):
    bossassit = models.ForeignKey(Boss, on_delete=models.CASCADE)
    user_ptr = models.OneToOneField(
        User,on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )
    class Meta:
        verbose_name = 'Assistant'
        verbose_name_plural = 'Assistants'
    def __str__(self):
        return f'Assitant {self.name} {self.last_name}'