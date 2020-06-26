from django.urls import path

from dictionary.views import DictionaryList, DictionaryCreateView, DictionaryDetailView, DictionaryUpdateView, DictionaryDeleteView

app_name='dictionary'

urlpatterns = [
    path('', DictionaryList.as_view(), name='list'),
    path('add/', DictionaryCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', DictionaryDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', DictionaryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', DictionaryDeleteView.as_view(), name='delete'),
]