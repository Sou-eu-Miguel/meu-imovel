from django.db import models
from django.urls import reverse

from ..imovel.models import Property


class Advertisement(models.Model):

    description     = models.TextField('description')
    price           = models.DecimalField('price', decimal_places= 2, max_digits=10)
    contact_phone   = models.CharField('contact_phone',max_length=12)
    contact_email   = models.EmailField('contact_email')

    # Foreign key
    imovel          = models.ForeignKey(Property, on_delete=False)

    def __str__(self):
        return self.description


    class Meta:
        verbose_name        = 'Advertisement'
        verbose_name_plural = 'Advertisements'
        ordering            = ['description', 'price']


    def get_absolute_url(self):
        return reverse('advertisement-read', kwargs={'pk': self.pk})
