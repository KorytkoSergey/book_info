
from django.urls import path, include

from django.views.generic import TemplateView
from book import views

app_name = 'book'

urlpatterns = [
    path('index/', TemplateView.as_view(template_name='book/index.html'), name='index'),
    path('book/<slug:slug>/', views.InfoCard.as_view(), {'list_type': 'book'}, name='book'),
    path('book_list/', views.TotalList.as_view(), {'list_type': 'book_list'}, name='book_list'),
    path('author_list/', views.TotalList.as_view(), {'list_type': 'author_list'}, name='author_list'),
    path('genre_list/', views.TotalList.as_view(), {'list_type': 'genre_list'}, name='genre_list'),
    path('author/<slug:slug>/', views.InfoCard.as_view(), {'list_type': 'author'}, name='author'),
    path('b_list', views.BookList.as_view(), name='book'),
]
