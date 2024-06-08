from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User (AbstractUser):
    national_id = models.BigIntegerField(null=True, blank=True)
    job_title = models.CharField(max_length=250, null=True, blank=True)
    is_admin = models.BooleanField(default=False, null=True, blank=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

class OTPCode(models.Model):
    otp = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True, null=True)
    valid_for = models.DateTimeField(null=True)
    verified = models.BooleanField(default=False)