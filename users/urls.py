from django.urls import path
from . import views


urlpatterns = [
    path(r'login/', views.login, name='login'),
    path(r'home/', views.home, name='home'),
]