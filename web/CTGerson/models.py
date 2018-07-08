from django.db import models
from django.utils import timezone


class Bus(models.Model):
    plate = models.CharField(max_length=8)
    line_number = models.CharField(max_length=5)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.plate


class Ocurrence(models.Model):
    busid = models.ForeignKey('CTGerson.Bus', on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    alert_time = models.TimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)
    response_time = models.TimeField(default=timezone.localtime)
    responder_id = models.ForeignKey('auth.User', on_delete=models.PROTECT, default=3)
    finish_time = models.TimeField(default=timezone.localtime)
    successfull = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
