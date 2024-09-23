from django.forms import ModelForm
from .models import EmailCampaign
from django import forms
from emailservice.models import EmailList



class EmailCampaignForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Campaign Name',
        'id': 'name'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Subject',
        'id': 'subject'
    }))
    email_list = forms.ModelChoiceField(queryset=EmailList.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'email_list'
    }))

    class Meta:
        model = EmailCampaign
        fields = ['name', 'subject', 'body', 'email_list']
        labels = {
            'name': 'Campaign Name',
            'subject': 'Email Subject',
            'body': 'Email Body',
            'email_list': 'Email List'
        }
        help_texts = {
            'name': 'Enter a name for the campaign',
            'subject': 'Enter the subject of the email',
            'body': 'Enter the body of the email',
            'email_list': 'Select the email list to send the email to'
        }
        error_messages = {
            'name': {
                'required': 'Please enter a name for the campaign'
            },
            'subject': {
                'required': 'Please enter the subject of the email'
            },
            'body': {
                'required': 'Please enter the body of the email'
            },
            'email_list': {
                'required': 'Please select an email list'
            }
        }


class CampaignDeleteForm(forms.Form):
    campine_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Campaign Name',
        'id': 'campine_name'
    }))

    def __init__(self, campaign, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.campaign = campaign

    def clean_campine_name(self):
        campine_name = self.cleaned_data['campine_name']
        print(campine_name)
        print(self.campaign.name)
        if campine_name != self.campaign.name:
            raise forms.ValidationError(f'"{campine_name}", The campaign name does not match')
        return campine_name
