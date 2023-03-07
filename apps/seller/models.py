from django.db import models
from apps.users.models import User
# Create your models here.
class Seller(User):
    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'
    user_ptr = models.OneToOneField(
        User,on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )
    