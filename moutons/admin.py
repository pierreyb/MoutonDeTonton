from django.contrib import admin
from django import forms
from .models import Lot


class LotAdminForm(forms.ModelForm):

    class Meta:
        model = Lot
        fields = '__all__'


class LotAdmin(admin.ModelAdmin):
    form = LotAdminForm
    list_display = ['name']
    readonly_fields = ['name']

admin.site.register(Lot, LotAdmin)


