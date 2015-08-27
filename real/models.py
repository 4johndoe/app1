from django.db import models

# Create your models here.

class Branche(models.Model):
	kod = models.IntegerField(default=0)
	name = models.CharField(max_length=200)

class Property(models.Model):
	kod = models.ForeignKey(Branche)
	address = models.CharField(max_length=200)
	square = models.IntegerField(default=0)