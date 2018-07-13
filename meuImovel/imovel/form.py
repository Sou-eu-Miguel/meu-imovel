from django import forms

from .models import Property
from _collections import OrderedDict

class PropertyForm(forms.ModelForm):
    form_fields = {}
    class Meta:
        model = Property
        exclude = ('updated', 'created')
        fields = ['description', 'square_meter', 'number_of_bedrooms', 'number_of_bathrooms']

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)

        self.form_fields['Descrição'] = self.fields['description']
        self.form_fields['Espaço (M²)'] = self.fields['square_meter']
        self.form_fields['N° de Quartos'] = self.fields['number_of_bedrooms']
        self.form_fields['N° de Banheiros'] = self.fields['number_of_bathrooms']

        self.form_fields['Descrição'].widget.attrs.update({
            'placeholder': 'ex: Apartamento'})


        self.fields = self.form_fields
