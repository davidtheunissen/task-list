from django.db import models
from datetime import datetime


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    deadline = models.DateTimeField(default=datetime.now)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name