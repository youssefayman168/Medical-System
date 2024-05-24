from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task


@shared_task(bind=False)
def mail_user(subject, message, email):
    """
    a method that sends a user an email
    NOTE: this method will run on another thread, so Django won't know anything about it or if it failed it not gonna
    break down the response
    """
    try:
        subject = subject
        message = message
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)
        print("EMAIL SENT")
    except Exception as e:
        print('send email error !')
        print(e)
