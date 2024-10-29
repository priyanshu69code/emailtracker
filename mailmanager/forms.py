from django import forms
from .models import EmailSetting

class EmailForm(forms.Form):
    gmail_address = forms.ModelMultipleChoiceField(
        queryset=EmailSetting.objects.all(),
        label='Select Gmail Address',
        widget=forms.SelectMultiple(attrs={
            'class': 'form-select',
        })
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['gmail_address'].queryset = EmailSetting.objects.filter(user=user)
