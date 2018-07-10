from django import forms
from .models import Bus, Occurrence


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ('plate', 'line_number', 'company')


class OccurrenceForm(forms.ModelForm):
    class Meta:
        model = Occurrence
        fields = ('successfull', 'notes')