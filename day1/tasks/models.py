from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True,max_length=1000)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    