from . import models

from rest_framework import serializers


class MoutonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Mouton
        fields = (
            'pk', 
            'sanitel_number', 
            'herbook_number', 
            'birth_date', 
            'sex', 
            'out_date', 
            'out_text', 
            'in_text', 
            'race', 
            'traitement', 
            'comment', 
            'birth_siblings', 
            'father', 
            'mother', 
            'name', 
            'birth_weight', 
            'one_month_weight', 
            'one_month_date', 
            'two_month_weight', 
            'two_month_date', 
            'third_weight', 
            'third_date', 
            'fourth_weight', 
            'fourth_date', 
            'sold_weight', 
            'slaughtered_weight', 
            'mouton_class', 
            'sold_value', 
            'origin_number', 
            'destination_number', 
            'qualification', 
            'genotype', 
            'birth', 
            'blood_test', 
        )


class LotSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Lot
        fields = (
            'pk', 
            'name', 
        )


class TreatmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Treatment
        fields = (
            'pk', 
            'comment', 
        )


class LutteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Lutte
        fields = (
            'pk', 
            'name_male', 
            'alive_number', 
            'dead_number', 
            'birth_weight_1', 
            'birth_weight_2', 
            'birth_weight_3', 
            'bred_number', 
            'sex', 
            'remark', 
            'lutte_type', 
            'code', 
        )


