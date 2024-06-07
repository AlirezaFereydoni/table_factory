from django.db.models import Model,DateTimeField,CharField,TextField,IntegerField,ImageField,ManyToManyField,CASCADE

# Create your models here.

class TimeStamp(Model): 
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)   
    
    class Meta:
        abstract = True


class Item(Model):
    name = CharField(max_length=100, blank=True, default=None)
    size = CharField(max_length=100)
    length = IntegerField()
    count = IntegerField()
    image = ImageField(null=True, blank=True )
    description = TextField(max_length=300, default=None, blank=True)
    
    
    def __str__(self):
        return f'{self.name} | {self.size} | {self.length} | {self.count}'
    
    
class MDF(Model):
    name = CharField(max_length=100)
    size = CharField(max_length=50)
    count = IntegerField()
    description = TextField(max_length=300)
 
    
    def __str__(self):
        return f'{self.name} | {self.size} | {self.count}'
    
class Section(Model): 
    name = CharField(max_length=100, blank=True, default=None)
    items = ManyToManyField(Item)
    mdf_items = ManyToManyField(MDF)
    image = ImageField(null=True)
   
    
    def __str__(self):
        return self.name
    
class Product(Model): 
    name = CharField(max_length=100, null=False, blank=False)
    description = TextField(max_length=300, null=True, blank=True)
    vision = ImageField()
    series = ManyToManyField(Section)
    
    def __str__(self):
        return f'{self.name} | {self.description}'
    
    