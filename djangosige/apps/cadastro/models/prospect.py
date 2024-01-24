# -*- coding: utf-8 -*-

from django.db import models


class Prospect(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)

    class Meta:
        verbose_name = "Prospect"

    def __unicode__(self):
        return u'%s / %s' % (self.nome_completo, self.cpf)

    def __str__(self):
        return u'%s / %s' % (self.nome_completo, self.cpf)
