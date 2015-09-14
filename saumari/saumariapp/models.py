from django.db import models

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Database structure

#Tyyp, Hind, Kirjeldus
#Pyksid, 10, Pyksid kitsamaks

class Type(models.Model):
    type = models.CharField(max_length=200)
    
    def __str__(self):
	   return self.type

class Clothing(models.Model):
    clothing_type = models.CharField(max_length=200)
    
    def __str__(self):
	   return self.clothing_type

class Listing(models.Model):
    type = models.ForeignKey(Type, default=1)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)

    def __str__(self):
	   return self.description

class Image(models.Model):
    image = models.ImageField()
    img_description = models.CharField(max_length=1000, default='none')
    price = models.IntegerField(default=0)
    img_type = models.ForeignKey(Clothing, default=1)
    
    def __str__(self):
	   return self.img_description
