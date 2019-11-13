from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    # This means that the UserProfileInfo has a OneToOneField to the User Model

    # Add any additional attribute you want
    portfolio_site = models.URLField(blank = True)
    # Url is optional
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank = True)

    def __str__(self):
        return self.user.username