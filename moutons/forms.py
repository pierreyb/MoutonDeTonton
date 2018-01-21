import re
from django import forms
from .models import Mouton, Treatment, Lutte


class MoutonForm(forms.ModelForm):
    class Meta:
        model = Mouton
        fields = ['sanitel_number', 'origin_number',
                  'name', 'birth_date', 'sex', 'race',
                  'in_text', 'in_date',
                  'birth_siblings', 'father', 'mother',
                  'genotype', 'lot_number',
                  'blood_test',
                  'traitement',
                  'comment'
                  ]

    def __init__(self, *args, **kwargs):
        super(MoutonForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget.attrs['placeholder'] = "dd/mm/yyyy"
        self.fields['in_date'].widget.attrs['placeholder'] = "dd/mm/yyyy"

        # clean_FIELDNAME(self) pour ajouter des validations pour un champ spécifique

    def clean_sanitel_number(self):
        # Remove non numeric character
        return re.sub(r"\D", "", self.cleaned_data['sanitel_number'])


class MoutonSortieForm(forms.ModelForm):
    class Meta:
        model = Mouton
        fields = ['sanitel_number', 'out_date', 'out_text', 'sold_weight', 'slaughtered_weight',
                  'mouton_class', 'sold_value', 'destination_number', 'qualification']

    def __init__(self, *args, **kwargs):
        super(MoutonSortieForm, self).__init__(*args, **kwargs)
        self.fields['sanitel_number'].disabled = True
        self.fields['out_date'].widget.attrs['placeholder'] = "dd/mm/yyyy"
        self.fields['out_date'].required = True


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['date', 'treatment', 'comment']

    def __init__(self, *args, **kwargs):
        super(TreatmentForm, self).__init__(*args, **kwargs)
        # self.fields['mouton_number'].widget = forms.HiddenInput()


class LutteForm(forms.ModelForm):
    class Meta:
        model = Lutte
        fields = ['date_lutte', 'mouton_number', 'male_number', 'name_male', 'alive_number', 'dead_number',
                  'birth_weight_1', 'birth_weight_2', 'birth_weight_3',
                  'bred_number', 'sex', 'remark', 'lutte_type', 'code']
