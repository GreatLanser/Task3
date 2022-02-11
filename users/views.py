from django.shortcuts import render
from .models import UserInformation

def login(request):
    return render(
        request,
        'users/login.html',
        context={
            'title': 'Log in'
        }
    )
def home(request):
    usernames = UserInformation.username
    emails = UserInformation.email
    status = UserInformation.status
    return render(
        request,
        'users/home.html',
        context={
            'title': 'Home page',
            'usernames': usernames,
            'emails': emails,
            'status': status,
        }
    )
# Create your views here.
