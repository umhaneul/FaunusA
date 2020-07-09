from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from dictionary.models import Dictionary


class DictionaryList(ListView):
    model = Dictionary
    # paginate_by = 9

    def get_queryset(self):
        search_animal_name = self.request.GET.get('search_animal_name', '')

        if search_animal_name == '':
            dictionary_list = self.model.objects.all()
        else:
            dictionary_list = self.model.objects.filter(animal_name__contains=search_animal_name)
        return dictionary_list

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if len(queryset) == 1:
            return redirect('dictionary:detail', queryset.first().pk)
        return super().get(request, *args, **kwargs)

class DictionaryPiscesList(ListView):
    model = Dictionary
    # paginate_by = 10
    template_name = 'dictionary/dictionary_p.html'
    def get_queryset(self):
        dictionary_list = self.model.objects.filter(kind='어류')
        return dictionary_list

class DictionaryAmphibiaList(ListView):
    model = Dictionary
    # paginate_by = 10
    template_name = 'dictionary/dictionary_a.html'
    def get_queryset(self):
        dictionary_list = self.model.objects.filter(kind='양서류')
        return dictionary_list

class DictionaryReptileList(ListView):
    model = Dictionary
    # paginate_by = 10
    template_name = 'dictionary/dictionary_r.html'
    def get_queryset(self):
        dictionary_list = self.model.objects.filter(kind='파충류')
        return dictionary_list

class DictionaryMammalList(ListView):
    model = Dictionary
    # paginate_by = 10
    template_name = 'dictionary/dictionary_m.html'
    def get_queryset(self):
        dictionary_list = self.model.objects.filter(kind='포유류')
        return dictionary_list

class DictionaryBirdList(ListView):
    model = Dictionary
    # paginate_by = 10
    template_name = 'dictionary/dictionary_b.html'
    def get_queryset(self):
        dictionary_list = self.model.objects.filter(kind='조류')
        return dictionary_list

class DictionaryInvertebrtesList(ListView):
    model = Dictionary
    # paginate_by = 10
    template_name = 'dictionary/dictionary_i.html'
    def get_queryset(self):
        dictionary_list = self.model.objects.filter(kind='무척추동물')
        return dictionary_list

class DictionaryCreateView(CreateView):
    model = Dictionary
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('dictionary:list')

class DictionaryDetailView(DetailView):
    model = Dictionary
    template_name = 'dictionary/dictionary_detail.html'

class DictionaryUpdateView(UpdateView):
    model = Dictionary
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('dictionary:list')

class DictionaryDeleteView(DeleteView):
    model = Dictionary
    success_url = reverse_lazy('dictionary:list')

