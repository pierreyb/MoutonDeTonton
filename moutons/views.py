import datetime

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mouton, Lot, Treatment, Lutte
from .forms import MoutonForm, MoutonSortieForm, TreatmentForm, LutteForm


class MoutonListView(ListView):
    model = Mouton
    queryset = Mouton.objects.filter(out_date__isnull = True)


class MoutonCreateView(LoginRequiredMixin, CreateView):
    model = Mouton
    form_class = MoutonForm


class MoutonDetailView(DetailView):
    model = Mouton


class MoutonUpdateView(LoginRequiredMixin, UpdateView):
    model = Mouton
    form_class = MoutonForm


class MoutonSortieView(LoginRequiredMixin, UpdateView):
    model = Mouton
    form_class = MoutonSortieForm
    template_name_suffix = '_sortie'

    def form_valid(self, form):
        form.instance.lot_number = None
        return super().form_valid(form)


class MoutonInventaireListView(ListView):
    model = Mouton
    template_name_suffix = '_inventaire_list'
    queryset = Mouton.objects.filter(out_date__isnull = False)


class TreatmentListView(ListView):
    model = Treatment


class TreatmentCreateView(LoginRequiredMixin, CreateView):
    model = Treatment
    form_class = TreatmentForm

    def get_initial(self):
        initial_data = super(TreatmentCreateView,self) .get_initial()
        initial_data['date'] = datetime.date.today()
        return initial_data

    # add the mouton_number before saving treatment
    # with validation of the mouton_number
    def form_valid(self, form):
        mouton = get_object_or_404(Mouton, pk=self.kwargs.get('mouton_number'))
        form.instance.mouton_number = mouton
        return super(TreatmentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TreatmentCreateView,self).get_context_data(**kwargs)
        context['my_mouton_number'] = self.kwargs.get('mouton_number')
        return context

    def get_success_url(self):
        return reverse_lazy('moutons_mouton_detail',args=[self.object.mouton_number_id])



class TreatmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Treatment
    form_class = TreatmentForm

    def get_context_data(self, **kwargs):
        context = super(TreatmentUpdateView,self).get_context_data(**kwargs)
        context['my_mouton_number'] = self.object.mouton_number_id
        return context

    def get_success_url(self):
        return reverse_lazy('moutons_mouton_detail',args=[self.object.mouton_number_id])



class LutteListView(ListView):
    model = Lutte


class LutteCreateView(LoginRequiredMixin, CreateView):
    model = Lutte
    form_class = LutteForm


class LutteDetailView(DetailView):
    model = Lutte


class LutteUpdateView(LoginRequiredMixin, UpdateView):
    model = Lutte
    form_class = LutteForm
