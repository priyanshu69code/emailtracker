from django.urls import path
from .views import track_email_open

app_name = 'tracker'

urlpatterns = [
    path('track-email-open/<str:tracking_id>/',
         track_email_open, name='track_email_open'),
]
