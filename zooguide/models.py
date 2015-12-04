from django.db import models

class Animals(models.Model):
    animal_name = models.CharField(max_length=35)
    animal_text = models.TextField()
    
class Exhibits(models.Model):
    exhibit_name = models.CharField(max_length=35)
    exhibit_text = models.TextField()

class Tips(models.Model):
    tip_title = models.CharField(max_length=35)
    tip_text = models.TextField()
    exhibits = models.ManyToManyField(Exhibits)
    tip_date = DateTimeField(auto_now)