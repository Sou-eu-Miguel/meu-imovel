from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Advertisement


class AdvertisementCreate(CreateView):
    model = Advertisement
    fields = ['nome', 'descricao', 'data_referencia']
    template_name = 'advertisement/form.html'


class AdvertisementDetail(DetailView):
    model = Advertisement
    template_name = 'advertisement/detail.html'


class AdvertisementUpdate(UpdateView):
    model = Advertisement
    fields = ['nome', 'descricao', 'data_referencia']
    success_url = reverse_lazy('advertisement-list')
    template_name = 'advertisement/form.html'


class AdvertisementDelete(DeleteView):
    model = Advertisement
    success_url = reverse_lazy('property-list')
    template_name = 'advertisement/delete.html'


class AdvertisementList(ListView):
    model = Advertisement
    template_name = 'advertisement/list.html'
