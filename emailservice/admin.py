from django.contrib import admin

# Register your models here.

from .models import Email, EmailList

admin.site.register(Email)
admin.site.register(EmailList)
