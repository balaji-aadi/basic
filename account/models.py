from django.db import models

class UserLogin(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.username
