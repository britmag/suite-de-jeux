# encoding: utf-8
from django.contrib import admin

# Register your models here.
from .models import OptionType, Option


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


class OptionTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Type d\'option', {'fields': ['type_text']}),
        ('Unité de mesure', {'fields': ['value_type']}),
    ]
    inlines = [OptionInline]
    list_display = ('type_text', 'value_type', 'count_options')


admin.site.register(OptionType, OptionTypeAdmin)
