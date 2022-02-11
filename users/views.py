from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import User


class UserListView(generic.ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users_list'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['last_login'] = 'This is just some data'
        return context


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'