from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField()
    is_complete =  models.BooleanField(default=False)