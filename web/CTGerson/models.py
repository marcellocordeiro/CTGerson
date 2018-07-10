from django.db import models
from django.utils import timezone


class Bus(models.Model):
    plate = models.CharField(max_length=8)
    line_number = models.CharField(max_length=5)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.plate

    class Meta:
        permissions = (("can_see_bus_list", "See bus list"),)


class Occurrence(models.Model):
    closed = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    bus = models.ForeignKey('CTGerson.Bus', on_delete=models.PROTECT, default=1)
    alert_time = models.TimeField(default=timezone.localtime)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    responded = models.BooleanField(default=False)
    response_time = models.TimeField(default=timezone.localtime)
    responder = models.ForeignKey('auth.User', on_delete=models.PROTECT, default=3)
    finish_time = models.TimeField(default=timezone.localtime)
    successfull = models.BooleanField(default=False)
    notes = models.TextField(blank=True)


class Distance(models.Model):
    officer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    bus = models.ForeignKey('CTGerson.Bus', on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return self.officer.username


class Meshblu(models.Model):
    bus = models.ForeignKey('CTGerson.Bus', on_delete=models.PROTECT, default=1)
    button = models.BooleanField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.bus.plate