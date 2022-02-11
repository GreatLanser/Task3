from django.shortcuts import render
from django.views import generic
from .models import UserInformation


def login(request):
    return render(
        request,
        'users/registration/../templates/registration/login.html',
        context={
            'title': 'Log in'
        }
    )


class UserListView(generic.ListView):
    model = UserInformation
    template_name = 'users/users.html'
    context_object_name = 'users_list'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['last_login'] = 'This is just some data'
        return context
