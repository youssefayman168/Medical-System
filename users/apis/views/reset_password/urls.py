from django.urls import path
from .send_otp import send_reset_otp
from .verify_password import verify_otp
from .reset_password import reset_password

urlpatterns = [
    path("send-otp/", send_reset_otp),
    path("verify-otp/", verify_otp),
    path("reset/", reset_password),
]