from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Property, Address
from ..core.service.gmaps.gmaps_utilities import Gmaps
from ..settings import MEDIA_ROOT


class PropertyForm(forms.ModelForm):

    latitude    = forms.CharField(widget=forms.HiddenInput(), required=True)
    longitude   = forms.CharField(widget=forms.HiddenInput(), required=True)

    class Meta:
        model = Property
        fields = ['description', 'square_meter', 'number_of_bedrooms', 'number_of_bathrooms','image','address']
        labels = {
            'description': _('Descrição'),
            'square_meter': _('Espaço (M²)'),
            'number_of_bedrooms': _('N° de Quartos'),
            'number_of_bathrooms': _('N° de Banheiros'),
            'image': _('Imagem'),
        }
        widgets = {
            'address': forms.HiddenInput(),
        }


    def clean(self):

        cleaned_data = super().clean()
        number_of_bedrooms  = cleaned_data.get("number_of_bedrooms")
        number_of_bathrooms = cleaned_data.get("number_of_bathrooms")
        latitude            = cleaned_data.get("latitude")
        longitude           = cleaned_data.get("longitude")

        if number_of_bedrooms is None:
            msg = "Quantidade de quartos inválida"
            self.add_error('number_of_bedrooms', msg)
            return self.cleaned_data

        if number_of_bathrooms is None:
            msg = "Quantidade de banheiros inválida"
            self.add_error('number_of_bathrooms', msg)
            return self.cleaned_data

        if latitude is None or longitude is None:
            msg = "Selecione a localização do Imóvel no Mapa"
            self._errors['latitude'] = msg

            return self.cleaned_data

        handle_uploaded_file(cleaned_data['image'])

        gmaps = Gmaps()
        data_address = gmaps.create_address(lat = latitude,lng = longitude)

        cleaned_data['address'] = Address.objects.create(
                                         street    =data_address['street'],
                                         number    =data_address['number'],
                                         zip_code  =data_address['zip_code'],
                                         latitude  =data_address['latitude'],
                                         longitude =data_address['longitude']
                                        )
        return self.cleaned_data


def handle_uploaded_file(f):
    with open(MEDIA_ROOT+'/images/property/'+f._name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)