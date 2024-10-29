from django.contrib import admin

# Register your models here.

from .models import EmailSetting

admin.site.register(EmailSetting)
