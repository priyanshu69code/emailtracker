from django.db import models
from django.conf import settings

class EmailSetting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='email_settings')
    gmail_address = models.EmailField(unique=True)
    app_password = models.CharField(max_length=100)  # Store securely

    def __str__(self):
        return f"{self.gmail_address} for {self.user.username}"
