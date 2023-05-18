from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls', namespace='book')),
    path('', include('reader.urls', namespace='reader')),
]
