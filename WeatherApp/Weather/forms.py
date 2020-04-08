from .models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta:
        Model = City
        fields = ['name']
        widgets = {'name': TextInput(
            attrs={'class': 'form-control', 'name': 'city', 'id': 'city', 'placeholder': 'Введите город'})}
