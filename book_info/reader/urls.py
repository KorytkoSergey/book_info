from django.urls import path, include
from django.views.generic import TemplateView
from reader import views

app_name = 'reader'

urlpatterns = [
    path('reader_create/', views.ReaderCreate.as_view(), name='reader_create'),

]
