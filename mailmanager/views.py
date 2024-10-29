from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import EmailForm
from utils import send_user_email
from emailservice


# def send_user_email(email_pk, subject, message, recipient_list):
#     try:
#         # Retrieve the user's email settings
#         email_settings = EmailSetting.objects.get(pk=email_pk)

#         # Configure the email backend settings dynamically
#         settings.EMAIL_HOST_USER = email_settings.gmail_address
#         settings.EMAIL_HOST_PASSWORD = email_settings.app_password

#         # Send the email
#         send_mail(
#             subject,
#             message,
#             settings.EMAIL_HOST_USER,
#             recipient_list,
#             fail_silently=False,
#         )

#         return "Email sent successfully."
#     except EmailSetting.DoesNotExist:
#         return "User email settings not found."
#     except Exception as e:
#         return f"An error occurred: {str(e)}"


@login_required
def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            gmail_address = form.cleaned_data['gmail_address']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_list = [email.strip() for email in form.cleaned_data['recipient_list'].split(',')]

            # Send the email
            result = send_user_email(gmail_address.pk, subject, message, recipient_list)

            return render(request, 'mailmanager/email_result.html', {'result': result})

    else:
        form = EmailForm(user=request.user)

    return render(request, 'mailmanager/send_email.html', {'form': form})

@login_required
def send_email_view(request):
    if request.method == 'POST':
        campine_pk = request.POST.get('campine_pk')
