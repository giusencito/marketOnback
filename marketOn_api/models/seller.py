from user import *
class Seller(UserProfile):
     user_ptr = models.OneToOneField(
        UserProfile,on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )