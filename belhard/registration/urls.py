from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import UserCreateView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
