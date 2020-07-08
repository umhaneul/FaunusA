from django.shortcuts import render
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
            # # 검색 결과가 1개일 때만 바로 설명문으로 넘어가고 검색 결과가 여러 가지일 경우에는 list가 나온다.
            # if dictionary_list == 1:
            #
            # else:
            dictionary_list = self.model.objects.filter(animal_name__contains=search_animal_name)
        return dictionary_list

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

class DictionaryUpdateView(UpdateView):
    model = Dictionary
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('dictionary:list')

class DictionaryDeleteView(DeleteView):
    model = Dictionary
    success_url = reverse_lazy('dictionary:list')

