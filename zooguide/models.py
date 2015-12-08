from django.db import models

class Animals(models.Model):
    exhibit_name = models.TextField(max_length=35, default='default')
    animal_name = models.CharField(max_length=35)
    
class Exhibits(models.Model):
    exhibit_name = models.CharField(max_length=35)
    exhibit_date = models.TextField(max_length=35, default='default')
    exhibit_cost = models.TextField(max_length=35, default='default')
    exhibit_awards = models.TextField(max_length=200, default='default')
    exhibit_latest = models.TextField(max_length=200, default='default')
    exhibit_ilink = models.TextField(max_length=200, default='default')

class Tips(models.Model):
    tip_title = models.CharField(max_length=35)
    tip_text = models.TextField()
    #exhibits = models.ManyToManyField(Exhibits)
    #tip_date = DateTimeField(auto_now)
    
class Schedule(models.Models):
    time = models.CharField(max_length=35)
    animal_encounter.TextField(max_length=100)
    location.TextField(max_length=100)
    