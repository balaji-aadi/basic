from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    isActive = models.BooleanField()
    
    def __str__(self):
        return self.name
