from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    size = models.CharField(max_length=100)
    length = models.IntegerField()
    count = models.IntegerField()
    image = models.ImageField( null=True, blank=True )
    description = models.TextField(max_length=300, default='', blank=True)
    
    
class MDF(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    count = models.IntegerField()
    

    