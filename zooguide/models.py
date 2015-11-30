from django.db import models

class Animals(models.Model)
     animal_name = models.CharField(max_length=35)
     animal_text = models.CharField(max_length=250)

class Exhibits(models.Model)
     exhibit_name = models.CharField(max_length=35)
     exhibit_text = models.CharField(max_length=250)

class Tips(models.Model)
     tip_title = models.CharField(max_length=35)
     tip_text = models.CharField(max_length=250)