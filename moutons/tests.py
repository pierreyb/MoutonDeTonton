import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Mouton, Lot, Treatment, Lutte
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_mouton(**kwargs):
    defaults = {}
    defaults["sanitel_number"] = "sanitel_number"
    defaults["herbook_number"] = "herbook_number"
    defaults["birth_date"] = "birth_date"
    defaults["sex"] = "sex"
    defaults["out_date"] = "out_date"
    defaults["out_text"] = "out_text"
    defaults["in_text"] = "in_text"
    defaults["race"] = "race"
    defaults["traitement"] = "traitement"
    defaults["comment"] = "comment"
    defaults["birth_siblings"] = "birth_siblings"
    defaults["father"] = "father"
    defaults["mother"] = "mother"
    defaults["name"] = "name"
    defaults["birth_weight"] = "birth_weight"
    defaults["one_month_weight"] = "one_month_weight"
    defaults["one_month_date"] = "one_month_date"
    defaults["two_month_weight"] = "two_month_weight"
    defaults["two_month_date"] = "two_month_date"
    defaults["third_weight"] = "third_weight"
    defaults["third_date"] = "third_date"
    defaults["fourth_weight"] = "fourth_weight"
    defaults["fourth_date"] = "fourth_date"
    defaults["sold_weight"] = "sold_weight"
    defaults["slaughtered_weight"] = "slaughtered_weight"
    defaults["mouton_class"] = "mouton_class"
    defaults["sold_value"] = "sold_value"
    defaults["origin_number"] = "origin_number"
    defaults["destination_number"] = "destination_number"
    defaults["qualification"] = "qualification"
    defaults["genotype"] = "genotype"
    defaults["birth"] = "birth"
    defaults["blood_test"] = "blood_test"
    defaults.update(**kwargs)
    if "lot_number" not in defaults:
        defaults["lot_number"] = create_'lot'()
    return Mouton.objects.create(**defaults)


def create_lot(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Lot.objects.create(**defaults)


def create_treatment(**kwargs):
    defaults = {}
    defaults["comment"] = "comment"
    defaults.update(**kwargs)
    if "mouton_number" not in defaults:
        defaults["mouton_number"] = create_mouton()
    return Treatment.objects.create(**defaults)


def create_lutte(**kwargs):
    defaults = {}
    defaults["name_male"] = "name_male"
    defaults["alive_number"] = "alive_number"
    defaults["dead_number"] = "dead_number"
    defaults["birth_weight_1"] = "birth_weight_1"
    defaults["birth_weight_2"] = "birth_weight_2"
    defaults["birth_weight_3"] = "birth_weight_3"
    defaults["bred_number"] = "bred_number"
    defaults["sex"] = "sex"
    defaults["remark"] = "remark"
    defaults["lutte_type"] = "lutte_type"
    defaults["code"] = "code"
    defaults.update(**kwargs)
    if "male_number" not in defaults:
        defaults["male_number"] = create_mouton()
    if "mouton_number" not in defaults:
        defaults["mouton_number"] = create_mouton()
    return Lutte.objects.create(**defaults)


class MoutonViewTest(unittest.TestCase):
    '''
    Tests for Mouton
    '''
    def setUp(self):
        self.client = Client()

    def test_list_mouton(self):
        url = reverse('moutons_mouton_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_mouton(self):
        url = reverse('moutons_mouton_create')
        data = {
            "sanitel_number": "sanitel_number",
            "herbook_number": "herbook_number",
            "birth_date": "birth_date",
            "sex": "sex",
            "out_date": "out_date",
            "out_text": "out_text",
            "in_text": "in_text",
            "race": "race",
            "traitement": "traitement",
            "comment": "comment",
            "birth_siblings": "birth_siblings",
            "father": "father",
            "mother": "mother",
            "name": "name",
            "birth_weight": "birth_weight",
            "one_month_weight": "one_month_weight",
            "one_month_date": "one_month_date",
            "two_month_weight": "two_month_weight",
            "two_month_date": "two_month_date",
            "third_weight": "third_weight",
            "third_date": "third_date",
            "fourth_weight": "fourth_weight",
            "fourth_date": "fourth_date",
            "sold_weight": "sold_weight",
            "slaughtered_weight": "slaughtered_weight",
            "mouton_class": "mouton_class",
            "sold_value": "sold_value",
            "origin_number": "origin_number",
            "destination_number": "destination_number",
            "qualification": "qualification",
            "genotype": "genotype",
            "birth": "birth",
            "blood_test": "blood_test",
            "lot_number": create_'lot'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_mouton(self):
        mouton = create_mouton()
        url = reverse('moutons_mouton_detail', args=[mouton.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_mouton(self):
        mouton = create_mouton()
        data = {
            "sanitel_number": "sanitel_number",
            "herbook_number": "herbook_number",
            "birth_date": "birth_date",
            "sex": "sex",
            "out_date": "out_date",
            "out_text": "out_text",
            "in_text": "in_text",
            "race": "race",
            "traitement": "traitement",
            "comment": "comment",
            "birth_siblings": "birth_siblings",
            "father": "father",
            "mother": "mother",
            "name": "name",
            "birth_weight": "birth_weight",
            "one_month_weight": "one_month_weight",
            "one_month_date": "one_month_date",
            "two_month_weight": "two_month_weight",
            "two_month_date": "two_month_date",
            "third_weight": "third_weight",
            "third_date": "third_date",
            "fourth_weight": "fourth_weight",
            "fourth_date": "fourth_date",
            "sold_weight": "sold_weight",
            "slaughtered_weight": "slaughtered_weight",
            "mouton_class": "mouton_class",
            "sold_value": "sold_value",
            "origin_number": "origin_number",
            "destination_number": "destination_number",
            "qualification": "qualification",
            "genotype": "genotype",
            "birth": "birth",
            "blood_test": "blood_test",
            "lot_number": create_'lot'().pk,
        }
        url = reverse('moutons_mouton_update', args=[mouton.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LotViewTest(unittest.TestCase):
    '''
    Tests for Lot
    '''
    def setUp(self):
        self.client = Client()

    def test_list_lot(self):
        url = reverse('moutons_lot_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_lot(self):
        url = reverse('moutons_lot_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_lot(self):
        lot = create_lot()
        url = reverse('moutons_lot_detail', args=[lot.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_lot(self):
        lot = create_lot()
        data = {
            "name": "name",
        }
        url = reverse('moutons_lot_update', args=[lot.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TreatmentViewTest(unittest.TestCase):
    '''
    Tests for Treatment
    '''
    def setUp(self):
        self.client = Client()

    def test_list_treatment(self):
        url = reverse('moutons_treatment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_treatment(self):
        url = reverse('moutons_treatment_create')
        data = {
            "comment": "comment",
            "mouton_number": create_mouton().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_treatment(self):
        treatment = create_treatment()
        url = reverse('moutons_treatment_detail', args=[treatment.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_treatment(self):
        treatment = create_treatment()
        data = {
            "comment": "comment",
            "mouton_number": create_mouton().pk,
        }
        url = reverse('moutons_treatment_update', args=[treatment.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LutteViewTest(unittest.TestCase):
    '''
    Tests for Lutte
    '''
    def setUp(self):
        self.client = Client()

    def test_list_lutte(self):
        url = reverse('moutons_lutte_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_lutte(self):
        url = reverse('moutons_lutte_create')
        data = {
            "name_male": "name_male",
            "alive_number": "alive_number",
            "dead_number": "dead_number",
            "birth_weight_1": "birth_weight_1",
            "birth_weight_2": "birth_weight_2",
            "birth_weight_3": "birth_weight_3",
            "bred_number": "bred_number",
            "sex": "sex",
            "remark": "remark",
            "lutte_type": "lutte_type",
            "code": "code",
            "male_number": create_mouton().pk,
            "mouton_number": create_mouton().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_lutte(self):
        lutte = create_lutte()
        url = reverse('moutons_lutte_detail', args=[lutte.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_lutte(self):
        lutte = create_lutte()
        data = {
            "name_male": "name_male",
            "alive_number": "alive_number",
            "dead_number": "dead_number",
            "birth_weight_1": "birth_weight_1",
            "birth_weight_2": "birth_weight_2",
            "birth_weight_3": "birth_weight_3",
            "bred_number": "bred_number",
            "sex": "sex",
            "remark": "remark",
            "lutte_type": "lutte_type",
            "code": "code",
            "male_number": create_mouton().pk,
            "mouton_number": create_mouton().pk,
        }
        url = reverse('moutons_lutte_update', args=[lutte.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


