from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100, blank=True, default=None)
    size = models.CharField(max_length=100)
    length = models.IntegerField(min=1, max=2000)
    count = models.IntegerField(min=1)
    image = models.ImageField(null=True, blank=True )
    description = models.TextField(max_length=300, default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return f'{self.name} | {self.size} | {self.length} | {self.count}'
    
    
class MDF(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    count = models.IntegerField(min=1)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name} | {self.size} | {self.count}'
    
class Section(models.Model): 
    name = models.CharField(max_length=100, blank=True, default=None)
    items = models.ManyToManyField(Item,on_delete= models.CASCADE)
    MDFs = models.ManyToManyField(MDF, on_delete= models.CASCADE)
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model): 
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=300, null=True, blank=True)
    vision = models.ImageField()
    series = models.ManyToManyField(Section, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name} | {self.description}'
    
    