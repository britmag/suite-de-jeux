# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class OptionType(models.Model):
    type_text = models.CharField('Type d\'option', max_length = 200)
    value_type = models.CharField('Unité de mesure', max_length = 100)

    def __str__(self):
        return self.type_text

    def count_options(self):
        options = Option.objects.filter(option_type__type_text__startswith=self.type_text)
        return len(options)

    count_options.admin_order_field = 'count_options'
    count_options.short_description = 'Nombre d\'options'


@python_2_unicode_compatible
class Option(models.Model):
    option_type = models.ForeignKey(OptionType, on_delete=models.CASCADE)
    option_text = models.CharField('Description', max_length = 200)
    option_value = models.IntegerField('Durée / Nombre', default = 10)
    option_weight = models.FloatField('Poids', default = 1.)

    def __str__(self):
        return self.option_text
