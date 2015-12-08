from django.db import models

class Animals(models.Model):
    exhibit_name = models.CharField(max_length=35, default='default')
    animal_name = models.CharField(max_length=35)
    
class Exhibits(models.Model):
    exhibit_name = models.CharField(max_length=35)
    exhibit_date = models.DateTimeField()
    exhibit_cost = models.IntegerField(blank=True, null=True)
    exhibit_awards = models.TextField(blank=True, null=True)
    exhibit_latest = models.TextField(blank=True, null=True)
    exhibit_ilink = models.URLField(blank=True, null=True)
    description = models.TextField()
    animals = models.ManyToManyField(Animals, blank=True, null=True)
    
class Schedule(models.Model):
    time = models.DateTimeField()
    title = models.CharField(max_length=100)
    location = models.ManyToManyField(Exhibits, blank=True, null=True)
    description = models.TextField()
    