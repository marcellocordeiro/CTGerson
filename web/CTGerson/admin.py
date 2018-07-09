from django.contrib import admin
from .models import Bus, Occurrence, Officer_location

# Register your models here.
admin.site.register(Bus)
admin.site.register(Occurrence)
admin.site.register(Officer_location)
