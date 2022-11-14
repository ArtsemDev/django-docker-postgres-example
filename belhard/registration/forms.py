from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )
    email = forms.EmailField(
        widget=forms.EmailInput()
    )
    username = forms.CharField(
        widget=forms.TextInput()
    )

    class Meta:
        model = User
        fields = ('username', 'email')
