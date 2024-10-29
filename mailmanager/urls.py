from django.urls import path
from . import views


app_name = 'mailmanager'


urlpatterns = [
    path("send",view=views.send_email_view,name="send"),
]
