from django.urls import path
from . import views


urlpatterns = [
    path(r'login/', views.login, name='login'),
    path(r'users/', views.UserListView.as_view(), name='users'),
]