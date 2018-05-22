from django import forms

from .models import City

class CityForm(forms.Form):    
    city = forms.ModelMultipleChoiceField(queryset=City.objects.all())
