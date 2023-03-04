from django import forms

from events.models import Events


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_name', 'event_date']

        widgets = {
            'event_name' : forms.TextInput(attrs={'required': 'False'}),
            'event_date' : forms.DateInput(attrs={'required': 'False'})
        }