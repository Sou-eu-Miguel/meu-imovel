from django.db import models
from django.urls import reverse

from ..imovel.models import Property


class Advertisement(models.Model):
    description     = models.CharField('description', max_length=80)
    price           = models.DecimalField('price', decimal_places= 2, max_digits=10)
    image           = models.ImageField('image',blank=True)

    # Foreign key
    imovel          = models.ForeignKey(Property, on_delete=False)

    def __str__(self):
        return self.description


    class Meta:
        verbose_name        = 'Advertisement'
        verbose_name_plural = 'Advertisements'
        ordering            = ['description', 'price','image']


    def get_absolute_url(self):
        return reverse('advertisement-read', kwargs={'pk': self.pk})
