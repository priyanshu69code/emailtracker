from django.urls import reverse_lazy
from .forms import CustomSignUpForm
from django.contrib.auth import login
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm, CustomSignUpForm, ProfileEditForm, CustomPasswordChangeForm
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User


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


class UserProfileView(DetailView, LoginRequiredMixin):
    model = User
    template_name = 'user/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return get_object_or_404(User, username=self.request.user.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profileeditform'] = ProfileEditForm(
            instance=self.request.user)
        context['passwordchangeform'] = CustomPasswordChangeForm(
            user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        profileeditform = ProfileEditForm(request.POST, instance=request.user)
        print(request.user)
        passwordchangeform = CustomPasswordChangeForm(
            request.POST)
        if profileeditform.is_valid():
            profileeditform.save()
        if passwordchangeform.is_valid():
            passwordchangeform.save()

        return super().get(request, *args, **kwargs)
