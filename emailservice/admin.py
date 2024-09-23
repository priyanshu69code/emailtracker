from django.contrib import admin

# Register your models here.

from .models import EmailCampaign, EmailList

admin.site.register(EmailCampaign)
admin.site.register(EmailList)
