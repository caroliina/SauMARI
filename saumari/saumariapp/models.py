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

class Listing(models.Model):
    type = models.ForeignKey(Type, default=1)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)

    def __str__(self):
	   return self.description
