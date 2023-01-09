from user import *
from boss import *
class Assistant(UserProfile):
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE)
    user_ptr = models.OneToOneField(
        UserProfile,on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )
     