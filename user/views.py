from django.urls import reverse_lazy
from .forms import CustomSignUpForm
from django.contrib.auth import login
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm, CustomSignUpForm
from django.urls import reverse
from django.shortcuts import render


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = "user/login.html"

    def get_success_url(self):
        return reverse('user:home')  # Redirect to the home page after login


class SignUpView(FormView):
    template_name = 'user/signup.html'
    form_class = CustomSignUpForm
    # Redirect to the home page after signup
    success_url = reverse_lazy('user:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def home(request):
    return render(request, 'home.html')
