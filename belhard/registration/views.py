from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView

from .forms import UserRegistrationForm


class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'registration/signup.html'
    success_url = '/'
