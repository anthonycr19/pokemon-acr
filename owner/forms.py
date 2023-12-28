from django.forms import ModelForm
from owner.models import Owner
from django import forms


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ('nombre', 'edad', 'pais', 'dni')

    # para dar estilos a los formularios que se trabajarán con Vistas Basadas en Clases
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
