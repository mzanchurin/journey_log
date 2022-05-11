from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Journey
from .forms import JourneyForm

class JourneyCreate(LoginRequiredMixin, CreateView):
    """View for creating Journey object."""
    model = Journey
    form_class = JourneyForm

    def get_success_url(self):
        return reverse_lazy('journey_detail', kwargs={'pk': self.object.id})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.request = self.request
        return form


class JourneyUpdate(UpdateView):
    """View for updating Journey object."""
    model = Journey
    form_class = JourneyForm
    success_url = reverse_lazy('journey_index')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.request = self.request
        return form



class JourneyDelete(DeleteView):
    """View for deleting Journey object."""
    model = Journey
    success_url = reverse_lazy('journey_index')


class JourneyList(ListView):
    """Вьюшка для отображения списка объектов RID."""
    model = Journey
    form_for_fields = JourneyForm
    fields_for_table = ['name', 'gosnum', 'gosdate', 'datesign', 'result_type', 'alleged_enforcement', 'ipccode']

