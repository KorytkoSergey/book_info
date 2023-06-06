from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from reader import models, forms
from django.shortcuts import redirect
from django.urls import reverse


class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context


class ReaderCreate(TitleMixin, CreateView):
    model = models.Reader
    template_name = 'reader/reader_create.html'
    form_class = forms.ReaderCreate
    success_url = reverse_lazy('reader:reader_list')


class SearchReader(TitleMixin, ListView):
    model = models.Reader
    template_name = 'reader/reader_list.html'
    title = 'Список читателей'

    def get_queryset(self):
        name = self.request.GET.get('name')
        qs = models.Reader.objects.all()
        if name:
            return qs.filter(name__icontains=name)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.ReaderSearch(self.request.GET or None)
        return context


class ReaderUpdate(TitleMixin, UpdateView):
    model = models.Reader
    template_name = 'reader/reader_create.html'
    fields = '__all__'
    success_url = reverse_lazy('reader:reader_list')


class ReaderDelete(TitleMixin, DeleteView):
    model = models.Reader
    template_name = 'reader/reader_del.html'
    success_url = reverse_lazy('reader:reader_list')


class UserLogin(TitleMixin, View):
    template_name = 'reader/login.html'

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index')
        return render(request, self.template_name)

    def get(self, request):
        return render(request, self.template_name)

def user_logout(request):
    logout(request)
    return redirect('/index')