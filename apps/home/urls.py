from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *
from .validate import *

urlpatterns = [
    # INDEX
    path("", index, name="index"),

    # VALIDATE
    url('validate/email/', validate_email, name='validate_email'),
    url('validate/user/', validate_user, name='validate_user'),
    url('validate/email-registered/', validate_email_registered, name='validate_email_registered'),
]