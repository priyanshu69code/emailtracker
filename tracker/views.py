from django.shortcuts import render

# Create your views here.

# tracker/views.py

from django.http import HttpResponse
from emailservice.models import Email, EmailOpen
import requests
from django.db.utils import IntegrityError


def track_email_open(request, tracking_id):
    email = Email.objects.filter(tracking_id=tracking_id).first()
    if email:
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')

        # Check if this open event already exists before making the API call
        if not EmailOpen.objects.filter(
            tracking_id=email,
            ip_address=ip_address,
            user_agent=user_agent
        ).exists():

            # Now, perform the API call since it's necessary
            location_info = requests.get(
                f"https://ipapi.co/{ip_address}/json/").json()
            city = location_info.get('city', "Unknown")
            region = location_info.get('region', "Unknown")
            country = location_info.get('country_name', "Unknown")
            isp = location_info.get('org', "Unknown")

            try:
                # Try to increase opens
                email.increase_opens(ip_address, user_agent,
                                     city, region, country, isp)
            except IntegrityError:
                # Handle any IntegrityError exceptions that might occur
                pass

    # Return a 1x1 transparent image
    image_data = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
    return HttpResponse(image_data, content_type='image/gif')
