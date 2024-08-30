from django.db import models

# Create your models here.

from django.db import models

class EmailOpen(models.Model):
    tracking_id = models.ForeignKey("emailservice.Email", on_delete=models.CASCADE)
    opened_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(unique=True)
    user_agent = models.TextField()
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    isp = models.CharField(max_length=255)

    def __str__(self):
        return self.ip_address
