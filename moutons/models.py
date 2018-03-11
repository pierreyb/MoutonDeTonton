from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from moutons.validators import sanitel_validator


class Mouton(models.Model):
    SEX = (
        ('F','F'),
        ('M','M'),
    )
    RACE = (
        ('BLEU DU MAINE','BLEU DU MAINE'),
        ('TEXEL','TEXEL'),
        ('BLEU TEXEL', 'BLEU TEXEL'),
    )
    SIBLING = (
        ('Simple','Simple'),
        ('Double', 'Double'),
        ('Triple', 'Triple'),
        ('Quadruple','Quadruple'),
    )

    OUT_CHOICES = (
        ('V', 'V'),
        ('A', 'A'),
        ('M', 'M'),
    )

    # Fields
    sanitel_number = CharField("n° Sanitel", max_length=16, unique=True, validators=[sanitel_validator], )
    herbook_number = CharField("n° Herbook", max_length=16, blank=True, null=True)
    birth_date = DateField("date de naissance", blank=True, null=True)
    sex = CharField("sexe", max_length=1, choices=SEX)
    out_date = DateField("date de sortie", blank=True, null=True)
    out_text = CharField("commentaire de sortie", max_length=5, blank=True, choices=OUT_CHOICES)
    in_date = DateField("date d'entrée", blank=True, null=True)
    in_text = CharField("commentaire d'entrée", max_length=5, blank=True)
    race = CharField(max_length=50, blank=True, choices=RACE)
    traitement = TextField(blank=True)
    comment = TextField("commentaire", blank=True)
    birth_siblings = CharField("naissance multiple", max_length=50, blank=True, choices=SIBLING)
    father = CharField("père", max_length=50, blank=True)
    mother = CharField("mère", max_length=50, blank=True)
    name = CharField("nom", max_length=50, blank=True)
    birth_date2 = DateField("date de naissance 2", blank=True, null=True)
    birth_weight = DecimalField("poids à la naissance", max_digits=6,decimal_places=3, blank=True, null=True)
    one_month_weight = DecimalField(max_digits=6,decimal_places=3, blank=True, null=True)
    one_month_date = DateField(blank=True, null=True)
    two_month_weight = DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    two_month_date = DateField(blank=True, null=True)
    third_weight = DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    third_date = DateField(blank=True, null=True)
    fourth_weight = DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    fourth_date = DateField(blank=True, null=True)
    sold_weight = DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    slaughtered_weight = DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    mouton_class = CharField(max_length=50, blank=True, null=True)
    sold_value = CharField(max_length=10, blank=True, null=True)
    origin_number = CharField(max_length=10, blank=True, null=True)
    destination_number = CharField(max_length=12, blank=True, null=True)
    qualification = CharField(max_length=50, blank=True, null=True)
    genotype = CharField(max_length=15, blank=True, null=True)
    birth_comment = CharField(max_length=15, blank=True, null=True)
    blood_test = TextField(blank=True, null=True)

    # Relationship Fields
    lot_number = ForeignKey('moutons.Lot', on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return u'%s' % self.sanitel_number

    def get_absolute_url(self):
        return reverse('moutons_mouton_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('moutons_mouton_update', args=(self.pk,))

    def get_sortie_url(self):
        return reverse('moutons_mouton_sortie', args=(self.pk,))


class Lot(models.Model):

    # Fields
    name = CharField(max_length=10, unique=True)


    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('moutons_lot_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('moutons_lot_update', args=(self.pk,))


class Treatment(models.Model):

    # Fields
    date = DateField(blank=True, null=True)
    treatment = TextField(blank=True)
    comment = TextField(blank=True)

    # Relationship Fields
    mouton_number = models.ForeignKey('moutons.Mouton', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('moutons_treatment_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('moutons_treatment_update', args=(self.pk,))


class Lutte(models.Model):

    # Relationship Fields
    mouton_number = models.ForeignKey('moutons.Mouton',
                                      on_delete=models.DO_NOTHING,
                                      limit_choices_to={'sex' : 'F'},
                                      related_name='+',
                                      verbose_name='N° Sanitel')
    male_number = models.ForeignKey('moutons.Mouton',
                                    on_delete=models.DO_NOTHING,
                                    limit_choices_to={'sex': 'M'},
                                    null=True, blank=True,related_name='+' ,
                                    verbose_name='numéro du male')

    # Fields
    date_lutte = DateField("date lutte", blank=True, null=True)
    name_male = CharField("nom du père", max_length=50)
    birth_date = DateField("date de naissance", blank=True, null=True)
    alive_number = IntegerField("nombre de vivant", blank=True, null=True)
    dead_number = IntegerField("nombre décès", blank=True, null=True)
    birth_weight_1 = CharField("poids naissance 1", max_length=50, blank=True)
    birth_weight_2 = CharField("poids naissance 2", max_length=50, blank=True)
    birth_weight_3 = CharField("poids naissance 3", max_length=50, blank=True)
    bred_number = IntegerField("nombre élevé", blank=True, null=True)
    sex = CharField("sexe", max_length=50, blank=True)
    remark = TextField("remarque", blank=True)
    lutte_type = CharField("type de lutte", max_length=5, default='1')
    code = CharField(max_length=5, blank=True)


    class Meta:
        ordering = ('-date_lutte',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('moutons_lutte_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('moutons_lutte_update', args=(self.pk,))


