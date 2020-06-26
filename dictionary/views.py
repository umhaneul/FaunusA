from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from dictionary.models import Dictionary


class DictionaryList(ListView):
    model = Dictionary
    paginate_by = 10

class DictionaryCreateView(CreateView):
    model = Dictionary
    fields = ['animal_name', 'level', 'age', 'size', 'eat', 'live', 'description']
    template_name_suffix = '_create'
    success_url = reverse_lazy('dictionary:list')

class DictionaryDetailView(DetailView):
    model = Dictionary

class DictionaryUpdateView(UpdateView):
    model = Dictionary
    fields = ['animal_name', 'level', 'age', 'size', 'eat', 'live', 'description']
    template_name_suffix = '_update'
    success_url = reverse_lazy('dictionary:list')

class DictionaryDeleteView(DeleteView):
    model = Dictionary
    success_url = reverse_lazy('dictionary:list')