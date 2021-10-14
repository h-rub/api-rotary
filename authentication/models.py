from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
        Profile user model
    """
    email = models.EmailField(max_length=150, unique=True)
    company = models.CharField(max_length=70, blank=True)
    address = models.CharField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    
    picture = models.ImageField(upload_to='users/pictures', 
            blank=True, 
            null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def get_full_name_user(self):
        return {'full_name': f"{self.first_name} {self.last_name}"}
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"