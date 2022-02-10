from django.shortcuts import render
from .models import UserInformation

def login(request):
    return render(
        request,
        'login.html',
        context={

        }
    )
# Create your views here.
