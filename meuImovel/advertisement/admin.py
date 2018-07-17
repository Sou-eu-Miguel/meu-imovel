from django.contrib import admin

# Register your models here.

from .models import Property,Advertisement
from ..imovel.models import Address

admin.site.register(Property)
admin.site.register(Advertisement)
admin.site.register(Address)
