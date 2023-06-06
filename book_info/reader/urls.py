from django.urls import path, include
from django.views.generic import TemplateView
from reader import views

app_name = 'reader'

urlpatterns = [
    path('reader_create/', views.ReaderCreate.as_view(), name='reader_create'),
    path('reader_list/', views.SearchReader.as_view(), name='reader_list'),
    path('reader_update/<slug:slug>/', views.ReaderUpdate.as_view(), name='reader_update'),
    path('reader_del/<slug:slug>/', views.ReaderDelete.as_view(), name='reader_del'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),

]
