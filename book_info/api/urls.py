from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api_book/', views.BookList.as_view()),
    path('api_author/<pk>', views.AuthorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)