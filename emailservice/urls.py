from django.urls import path
from . import views

app_name = 'campain'

urlpatterns = [
    path('create', view=views.CreateNewCampain.as_view(),
         name='create'),
    path('email_list', view=views.EmailList.as_view(),name='email_list'),
    # Add more paths here
    path('detail/<int:pk>', view=views.EmailDetail.as_view(),name='email_detail'),
    path('update/<int:pk>', view=views.EmailUpdate.as_view(),name='update'),
    path('delete/<int:pk>', view=views.EmailDelete.as_view(),name='delete'),
]
