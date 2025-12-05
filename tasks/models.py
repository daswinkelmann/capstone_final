from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Task(models.Model):
#     pass

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]

    STATUS_CHOICES = [
        ('TODO', 'To-do'),
        ('DONE', 'Done'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='TODO')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
