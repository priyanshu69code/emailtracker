from django.shortcuts import render

# Create your views here.

# tracker/views.py

from django.http import HttpResponse
from emailservice.models import EmailCampaign, EmailOpen
import requests
from django.db.utils import IntegrityError


import requests
from django.http import HttpResponse
from django.db import IntegrityError

def track_email_open(request, tracking_id):
    email = EmailCampaign.objects.filter(tracking_id=tracking_id).first()
    if email:
        # Attempt to get the IP from X-Forwarded-For if behind a proxy, else use REMOTE_ADDR
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip_address:
            # X-Forwarded-For can have multiple IPs, take the first one
            ip_address = ip_address.split(',')[0]
        else:
            # Use REMOTE_ADDR if X-Forwarded-For is not present
            ip_address = request.META.get('REMOTE_ADDR')

        # Handle localhost scenario where the IP is 127.0.0.1 (development environment)
        if ip_address == '127.0.0.1':
            ip_address = '152.59.142.160'  # Replace with your actual public IP for testing

        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')

        # Check if this open event already exists before making the API call
        if not EmailOpen.objects.filter(
            tracking_id=email,
            ip_address=ip_address,
            user_agent=user_agent
        ).exists():
            # Fetch location info from the IP address
            try:
                location_info = requests.get(
                    f"https://ipapi.co/{ip_address}/json/"
                ).json()

                city = location_info.get('city', "Unknown")
                region = location_info.get('region', "Unknown")
                country = location_info.get('country_name', "Unknown")
                isp = location_info.get('org', "Unknown")
            except requests.RequestException:
                # Handle errors like network issues, or invalid IP address
                city, region, country, isp = "Unknown", "Unknown", "Unknown", "Unknown"

            try:
                # Try to increase opens, while handling any potential IntegrityError
                email.increase_opens(ip_address, user_agent, city, region, country, isp)
            except IntegrityError:
                # Handle any IntegrityError exceptions that might occur
                pass

    # Return a 1x1 transparent image (used for tracking)
    image_data = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
    return HttpResponse(image_data, content_type='image/gif')
