from django.db.models import F
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth import models
from django import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from user.models import User, Subject, Grade


class MilibalLoginView(auth_views.LoginView):
    model = User
    fields = ['id', 'password']
    template_name = 'user/milibal_login.html'
    success_url = reverse_lazy('milibal:index')


class MilibalAddUserView(CreateView):
    model = User
    fields = '__all__'
    template_name = 'user/milibal_join.html'
    # success_url = reverse_lazy('milibal:list')


class MilibalReadUserView(DetailView):
    model = User
    template_name = 'user/milibal_user.html'


class MilibalEditUserView(UpdateView):
    model = User
    fields = '__all__'  # <form>
    template_name = 'user/milibal_editUser.html'
    # success_url = reverse_lazy('bookmark:list')


class MilibalDeleteUserView(DeleteView):
    model = User
    template_name = 'user/milibal_confirm_deleteUser.html'
