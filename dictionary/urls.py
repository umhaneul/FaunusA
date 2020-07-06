from django.urls import path

from dictionary.views import DictionaryList, DictionaryCreateView, DictionaryDetailView, DictionaryUpdateView, \
    DictionaryDeleteView, DictionaryAmphibiaList, DictionaryBirdList, DictionaryInvertebrtesList, DictionaryMammalList, \
    DictionaryReptileList, DictionaryPiscesList
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name='dictionary'

urlpatterns = [
    path('', DictionaryList.as_view(), name='list'),
    path('add/', DictionaryCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', DictionaryDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', DictionaryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', DictionaryDeleteView.as_view(), name='delete'),
    path('a/', DictionaryAmphibiaList.as_view(), name='a'),
    path('b/', DictionaryBirdList.as_view(), name='b'),
    path('i/', DictionaryInvertebrtesList.as_view(), name='i'),
    path('m/', DictionaryMammalList.as_view(), name='m'),
    path('r/', DictionaryReptileList.as_view(), name='r'),
    path('p/', DictionaryPiscesList.as_view(), name='p'),

]

urlpatterns += staticfiles_urlpatterns()