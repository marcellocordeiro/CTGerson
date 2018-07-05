from django.db import models
from django.utils import timezone

class Bus(models.Model):
    plate = models.CharField(max_length = 8)
    linenumber = models.CharField(max_length = 5)
    company = models.CharField(max_length = 100)

    def __str__(self):
        return self.plate

#class Ocurrence(models.Model):
#    busid = models.ForeignKey('CTGerson.Bus')
