# Generated by Django 5.1.1 on 2024-09-11 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailservice', '0003_remove_email_email_list_emailcampaign'),
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailopen',
            name='tracking_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emailservice.emailcampaign'),
        ),
    ]
