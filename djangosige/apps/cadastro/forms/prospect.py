# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from djangosige.apps.cadastro.models import Prospect


class ProspectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ProspectForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Prospect
        fields = ('nome_completo', 'cpf', )
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control', 'data-mask':'000.000.000-70'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome_completo': _('Nome completo'),
            'cpf': _('CPF'),
        }