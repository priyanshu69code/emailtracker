# Generated by Django 5.1.1 on 2024-09-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, default='profile/default.jpg', null=True, upload_to='profile/'),
        ),
    ]
