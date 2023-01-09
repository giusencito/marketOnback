from user import *
 
class Boss(UserProfile):
     user_ptr = models.OneToOneField(
        UserProfile,on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )
 