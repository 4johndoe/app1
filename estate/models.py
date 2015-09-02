from django.db import models

# Create your models here.
class Filiya(models.Model):
    kod = models.IntegerField
    name = models.CharField(max_length=200)

class Estate(models.Model):
    owner = models.ForeignKey(Filiya)
    square = models.IntegerField
    address = models.CharField(max_length=200)

class Photo(models.Model):
    whose = models.ForeignKey(Estate)
    file = models.FilePathField