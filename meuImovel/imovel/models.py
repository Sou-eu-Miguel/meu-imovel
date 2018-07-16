from django.db import models

class Address(models.Model):
    street      = models.CharField('street', max_length=60)
    number      = models.CharField('number', max_length=10, blank = True)
    zip_code    = models.CharField('zip_code', max_length=60, blank = True)
    latitude    = models.DecimalField('latitude',max_digits= 20,decimal_places = 18)
    longitude   = models.DecimalField('longitude',max_digits= 20,decimal_places = 18)

    def __str__(self):
        return "{} - {} ".format(self.street, self.number)


class Property(models.Model):
    description         = models.CharField('description', max_length=60)
    square_meter        = models.PositiveSmallIntegerField('square_meter')
    number_of_bedrooms  = models.PositiveSmallIntegerField('number_of_bedrooms')
    number_of_bathrooms = models.PositiveSmallIntegerField('number_of_bathrooms')
    image = models.ImageField('image',upload_to='images/property')

    #Foreign key
    address             = models.ForeignKey(Address, on_delete=True, blank=True)


    def __str__(self):
        return self.description


    class Meta:
        verbose_name        = 'Property'
        verbose_name_plural = 'properties'
        ordering            = ['description', 'square_meter','number_of_bathrooms']
