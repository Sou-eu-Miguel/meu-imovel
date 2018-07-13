from django.db import models
from django.urls import reverse


class Address(models.Model):
    street      = models.CharField('street', max_length=60)
    number      = models.CharField('number', max_length=10, blank = True)
    zip_code    = models.CharField('zip_code', max_length=60, blank = True)
    latitude    = models.BigIntegerField('latitude')
    longitude   = models.BigIntegerField('longitude')

    def __str__(self):
        return "%s - %s ".format(self.street, self.number)


class Property(models.Model):
    name                = models.CharField('Name', max_length=60)
    square_meter        = models.IntegerField('square_meter')
    number_of_bedrooms  = models.PositiveSmallIntegerField('number_of_bedrooms',blank=True)
    number_of_bathrooms = models.PositiveSmallIntegerField('number_of_bathrooms',blank=True)

    #Foreign key
    address             = models.ForeignKey(Address, on_delete=False)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name        = 'Property'
        verbose_name_plural = 'properties'
        ordering            = ['name', 'square_meter','number_of_bathrooms']


    def get_absolute_url(self):
        return reverse('property-read', kwargs={'pk': self.pk})
