from django.db import models

# Create your models here.

class Paitent(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    document_number = models.BigIntegerField()
    date_order_delivered = models.DateField(null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    