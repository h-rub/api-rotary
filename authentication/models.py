from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import DO_NOTHING

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


class CustomUser(AbstractUser):
    """
        Profile user model
    """
    email = models.EmailField(max_length=150, unique=True)
    company = models.CharField(max_length=70, blank=True)
    address = models.CharField(max_length=200, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def get_full_name_user(self):
        return {'full_name': f"{self.first_name} {self.last_name}"}
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='user_profile', on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', 
            blank=True, 
            null=True)