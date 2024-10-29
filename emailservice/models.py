from django.db import models
from django.db.utils import IntegrityError

# Create your models here.
from tracker.models import EmailOpen
from django.urls import reverse
import uuid
from ckeditor.fields import RichTextField


class EmailCampaign(models.Model):
    name = models.CharField(max_length=255)
    tracking_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=255)
    body = RichTextField()
    number_of_opens = models.IntegerField(default=0)
    email_list = models.ForeignKey(
        'EmailList', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    camping_email = models.OneToOneField('mailmanager.EmailSetting', blank=True, related_name='camping_email',on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def increase_opens(self, ip_address, user_agent="Unknown", city="Unknown", region="Unkown", country="Unkown", isp="Unknown"):
        try:
            EmailOpen.objects.create(
                tracking_id=self,
                ip_address=ip_address,
                user_agent=user_agent,
                city=city,
                region=region,
                country=country,
                isp=isp,
            )
            self.number_of_opens += 1
            self.save()
        except IntegrityError:
            pass

    def get_absolute_url(self):
        return reverse('tracker:track_email_open', kwargs={'tracking_id': self.tracking_id})

    def create_tracker(self):
        self.body += f'<img src="{self.get_absolute_url()}" alt="Email Open Tracker" width="1" height="1" style="display:none;">'
        self.save()

    def save(self, *args, **kwargs):
        obj = super().save(*args, **kwargs)
        if not self.body.__contains__(self.get_absolute_url()):
            self.create_tracker()
        return obj


class EmailList(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='email_lists/',
                            default='profile_pics/default.jpg')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
