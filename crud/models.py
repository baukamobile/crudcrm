from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=timezone.now())
    finish_time = models.DateTimeField()
    is_complete =  models.BooleanField(default=False)


    def __str__(self):
        return f'{self.title} started at {self.start_time}'
    def formatted_start_time(self):
        return self.start_time.strftime('%d.%m %H:%M')
    formatted_start_time.short_description = 'Start Time'