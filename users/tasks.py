from celery import shared_task
from .models import User, OTPCode
from django.utils import timezone
from datetime import timedelta, datetime
from globals.mailer import mail_user
from globals.generate_otp import generate_otp

@shared_task(bind=False)
def send_otp(email):
    print("EMAIL:", email)
    try:
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print("Couldn't find the user")
        last_otp_code = OTPCode.objects.filter(user=user).last()
        if last_otp_code:
            last_otp_code.delete()
        otp_code = generate_otp()
        print("OTP:", otp_code)
        code = OTPCode.objects.create(
            user=user,
            valid_for=timezone.now() + timedelta(minutes=3),
            otp=otp_code
        )
        message = f"Welcome in SEC! this your OTP code: {code.otp}, please use it to restore your password, never share it with anyone, even us won't ask you about it"
        mail_user.delay(subject="Password Reset OTP",
                         message=message, email=user.email)
    except Exception as e:
        print("an error occurred while sending the user the OTP", e)