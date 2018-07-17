from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .form import AdvertisementForm
from .models import Advertisement
from ..core.service.gmaps.gmaps_utilities import Gmaps


@method_decorator(login_required, name='dispatch')
class AdvertisementCreate(CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'advertisement/form.html'



class AdvertisementDetail(DetailView):
    model = Advertisement
    template_name = 'advertisement/detail.html'


class AdvertisementUpdate(UpdateView):
    model = Advertisement
    fields = ['description', 'price', 'imovel']
    success_url = reverse_lazy('advertisement-list')
    template_name = 'advertisement/form.html'


class AdvertisementDelete(DeleteView):
    model = Advertisement
    success_url = reverse_lazy('advertisement-list')
    template_name = 'advertisement/delete.html'


class AdvertisementList(ListView):
    model = Advertisement
    template_name = 'advertisement/list.html'


def listUpcoming(request):
    template_name = 'advertisement/list.html'
    context = {}
    if request.POST:
        descricao_endereco = request.POST.get('endereco_cliente')

        if descricao_endereco:

            gmaps = Gmaps()
            endereco = gmaps.create_address_reverse(descricao_endereco)
            object_list = gmaps.shorter_distance_address(current_address = endereco,
                                           destination_address=Advertisement.objects.all())
            context['object_list'] = object_list
        else:
            context['object_list'] = Advertisement.objects.all()
    else:
        context['object_list'] = Advertisement.objects.all()

    return render(request, template_name, context=context)
