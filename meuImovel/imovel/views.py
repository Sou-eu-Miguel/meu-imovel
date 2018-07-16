from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .form import PropertyForm
from .models import Property


# Create your views here.

#@method_decorator(login_required, name='dispatch')
class PropertyCreate(CreateView):
    model = Property
    form_class = PropertyForm
    success_url = reverse_lazy('advertisement-create')
    template_name = 'property/form.html'

#@method_decorator(login_required, name='dispatch')
class PropertyDetail(DetailView):
    model = Property
    template_name = 'property/detail.html'


#@method_decorator(login_required, name='dispatch')
class PropertyUpdate(UpdateView):
    model = Property
    fields = ['nome', 'descricao', 'data_referencia']
    success_url = reverse_lazy('advertisement-list')
    template_name = 'property/form.html'


#@method_decorator(login_required, name='dispatch')
class PropertyDelete(DeleteView):
    model = Property
    success_url = reverse_lazy('advertisement-list')
    template_name = 'property/delete.html'
