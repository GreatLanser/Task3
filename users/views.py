from django.shortcuts import render
from django.views import generic
from .models import Users, change_user
from .forms import UserRegistrationForm


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
            keys = list(request.POST.keys())
            action = keys[1]
            users_id = keys[3:] if 'select_all' in keys else keys[2:]
            for user_id in users_id:
                change_user(action, user_id)
            return render(request, 'users/status_change.html')


class UserListView(generic.ListView):
    model = Users
    template_name = 'users/users.html'
    context_object_name = 'users_list'
