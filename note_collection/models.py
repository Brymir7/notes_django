from time import timezone
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
class Note(models.Model):  
    note_name = models.CharField(max_length=35, default='')
    note_text = models.TextField(blank=True, default='')
    pub_date = models.DateTimeField('date published', default=timezone.now())
    def __str__(self):
        return self.note_name
class Day(models.Model):
    day_name = models.CharField(max_length=35, default='01')
    day_text = models.TextField(max_length=200, default='')
    attached_notes = models.ManyToManyField(Note, default=None)
    def __str__(self):
        return self.day_name
class Month(models.Model):
    month_name = models.CharField(max_length=35, default='')
    days_amount = models.IntegerField(default='1')
    month_text = models.TextField(blank=True, default='')  
    days = models.ManyToManyField(Day, default=None) 
    def __str__(self):
        return self.month_name    

    