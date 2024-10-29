# Generated by Django 5.1.1 on 2024-10-29 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailservice', '0005_emailcampaign_camping_email'),
        ('mailmanager', '0002_alter_emailsetting_gmail_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailcampaign',
            name='camping_email',
        ),
        migrations.AddField(
            model_name='emailcampaign',
            name='camping_email',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='camping_email', to='mailmanager.emailsetting'),
        ),
    ]