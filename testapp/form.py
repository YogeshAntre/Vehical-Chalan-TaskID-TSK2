from django import forms
from .models import Vehicle, Chalan

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['registration_number', 'make', 'model', 'color', 'year']

class ChalanForm(forms.ModelForm):
    class Meta:
        model = Chalan
        fields = ['vehicle', 'amount', 'date', 'description']

