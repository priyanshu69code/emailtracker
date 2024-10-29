from django.core.mail import send_mail
from django.conf import settings
from mailmanager.models import EmailSetting


def send_user_email(email_pk, subject, message, recipient_list):
    try:
        # Retrieve the user's email settings
        email_settings = EmailSetting.objects.get(pk=email_pk)

        # Configure the email backend settings dynamically
        settings.EMAIL_HOST_USER = email_settings.gmail_address
        settings.EMAIL_HOST_PASSWORD = email_settings.app_password

        # Send the email
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False,
        )

        return "Email sent successfully."
    except EmailSetting.DoesNotExist:
        return "User email settings not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"
