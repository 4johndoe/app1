from django.db import models

# Create your models here.
class Filiya(models.Model):
    kod = models.IntegerField(default=0)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Estate(models.Model):
    owner = models.ForeignKey(Filiya)
    square = models.IntegerField(default=0)
    address = models.CharField(max_length=200)

class Photo(models.Model):
    whose = models.ForeignKey(Estate)
    file = models.FilePathField(default=0)