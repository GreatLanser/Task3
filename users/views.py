from django.shortcuts import render
from django.views import generic
from .models import Users
from .forms import UserRegistrationForm
from django.http import HttpRequest, HttpResponse


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/signup_confirm.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'user_form': user_form})


def status_change(request):
    if request.method == 'POST':
        if request.POST:
            content = request.POST.get('unblock', 'not')
            return render(request, 'users/status_change.html', {
                'title': 'hehe',
                'content': content,
            })


class UserListView(generic.ListView):
    model = Users
    template_name = 'users/users.html'
    context_object_name = 'users_list'

