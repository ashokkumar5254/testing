from django import forms
from .models import *
class CoordinatesForm(forms.ModelForm):
    class Meta:
        model = coordinates_model
        fields = '__all__'
