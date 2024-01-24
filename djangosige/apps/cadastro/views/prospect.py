# -*- coding: utf-8 -*-

from django.urls import reverse_lazy
from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView
from djangosige.apps.cadastro.forms import ProspectForm
from djangosige.apps.cadastro.models import Prospect

class AdicionarOutrosBaseView(CustomCreateView):
    template_name = "base/popup_form.html"

    def get_context_data(self, **kwargs):
        context = super(AdicionarOutrosBaseView, self).get_context_data(**kwargs)
        context['titulo'] = 'Adicionar ' + self.model.__name__
        return context


class EditarOutrosBaseView(CustomUpdateView):
    template_name = "base/popup_form.html"

    def get_context_data(self, **kwargs):
        context = super(EditarOutrosBaseView,
                        self).get_context_data(**kwargs)
        context['titulo'] = 'Editar {0}: {1}'.format(self.model.__name__, str(self.object))
        return context


class AdicionarProspectView(AdicionarOutrosBaseView):
    form_class = ProspectForm
    model = Prospect
    success_url = reverse_lazy('cadastro:addprospectview')
    permission_codename = 'add_prospect'


class ProspectListView(CustomListView):
    model = Prospect
    template_name = 'cadastro/prospect/prospect_list.html'
    context_object_name = 'all_prospects'
    success_url = reverse_lazy('cadastro:listaprospectsview')
    permission_codename = 'view_prospect'


class EditarProspectView(EditarOutrosBaseView):
    form_class = ProspectForm
    model = Prospect
    success_url = reverse_lazy('cadastro:listaprospectsview')
    permission_codename = 'change_prospect'