from django.db import models
from django.db.utils import IntegrityError

# Create your models here.
from tracker.models import EmailOpen
from django.urls import reverse
import uuid


class Email(models.Model):
    recipient_email = models.CharField(max_length=255)
    tracking_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    number_of_opens = models.IntegerField(default=0)
    email_list = models.ForeignKey(
        'EmailList', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.recipient_email

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


class EmailList(models.Model):
    name = models.CharField(max_length=255)
    emails = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
