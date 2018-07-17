from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['price','contact_phone','contact_email', 'imovel','description']
        labels = {
            'description': _('Descrição'),
            'price': _('Preço'),
            'contact_phone': _('Telefone de Contato'),
            'contact_email': _('E-Mail de Contato'),
            'imovel': _('Imovel')
        }
