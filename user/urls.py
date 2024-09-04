from django.urls import path
from .views import CustomLoginView, SignUpView, home

app_name = 'user'

urlpatterns = [
    path("login", CustomLoginView.as_view(), name="login"),
    path("register", SignUpView.as_view(), name="register"),
    path("home", home, name="home"),
]
