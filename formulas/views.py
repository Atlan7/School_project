from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .models import Theme, Formula


class ViewThemes(ListView):
    model = Theme
    template_name = 'formulas/view_themes.html'
    context_object_name = 'themes'


class ViewFormulasAboutTheme(ListView):
    template_name = 'formulas/view_formulas.html'
    context_object_name = 'formulas'

    def queryset(self):
        return Formula.objects.filter(theme_id=self.kwargs['theme_pk']).order_by('position')
