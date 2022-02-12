from django.urls import path, include
from . import views


urlpatterns = [
    path(r'', include('django.contrib.auth.urls'), name='login'),
    path(r'signup/', views.register, name='signup'),
    path(r'users/', views.UserListView.as_view(), name='users'),
]