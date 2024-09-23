from .models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email address',
        'id': 'email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'id': 'password'
    }))


class CustomSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email address',
        'id': 'email'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'id': 'username'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'id': 'password1'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
        'id': 'password2'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'id': 'first_name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
        'id': 'last_name'
    }))

    class Meta:
        model = User
        fields = ('email', 'username', "first_name",
                  "last_name", 'password1', 'password2')


class ProfileEditForm(UserChangeForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'style': 'height: 100px'}), required=False)
    company = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    job = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    country = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    twitter = forms.URLField(widget=forms.URLInput(
        attrs={'class': 'form-control'}), required=False)
    linkedin = forms.URLField(widget=forms.URLInput(
        attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = User
        fields = ('about', 'first_name', 'last_name', 'company', 'job', 'country',
                  'address', 'phone', 'email', 'twitter', 'linkedin')
        exclude = ('password', 'last_login', 'is_superuser', 'is_staff',
                   'is_active', 'date_joined', 'groups', 'user_permissions')


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'id': 'currentPassword'}))
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'id': 'newPassword'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'id': 'renewPassword'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
