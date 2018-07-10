from django.contrib import admin
from .models import Bus, Occurrence, Distance, Meshblu

# Register your models here.
admin.site.register(Bus)
admin.site.register(Occurrence)
admin.site.register(Distance)
admin.site.register(Meshblu)
