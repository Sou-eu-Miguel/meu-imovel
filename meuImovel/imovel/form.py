from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Property


class PropertyForm(forms.ModelForm):
    form_fields = {}

    class Meta:
        model = Property
        fields = ['description', 'square_meter', 'number_of_bedrooms', 'number_of_bathrooms']
        labels = {
            'description': _('Descrição'),
            'square_meter': _('Espaço (M²)'),
            'number_of_bedrooms': _('N° de Quartos'),
            'number_of_bathrooms': _('N° de Banheiros'),
        }

    def clean(self):
        cleaned_data = super().clean()
        number_of_bedrooms = cleaned_data.get("number_of_bedrooms")
        number_of_bathrooms = cleaned_data.get("number_of_bathrooms")
        latitude = cleaned_data.get("latitude")
        longitude = cleaned_data.get("longitude")

        if number_of_bedrooms is None:
            msg = "Quantidade de quartos inválida"
            self.add_error('number_of_bedrooms', msg)
        if number_of_bathrooms is None:
            msg = "Quantidade de banheiros inválida"
            self.add_error('number_of_bathrooms', msg)
