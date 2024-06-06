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
    

    
class Section(models.Model): 
    name = models.CharField(max_length=100, blank=True, default='')
    items = models.ManyToManyField(Item,on_delete= models.CASCADE)
    MDFs = models.ManyToManyField(MDF, on_delete= models.CASCADE)
    image = models.ImageField(null=True)
    
