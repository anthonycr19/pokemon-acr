from django.forms import ModelForm
from owner.models import Owner


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ('nombre', 'edad', 'pais', 'dni')
