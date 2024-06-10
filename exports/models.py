from django.db import models

# Create your models here.

class Export(models.Model):
    date = models.DateField(null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    receiver_name = models.CharField(max_length=300)
    attachment = models.FileField(upload_to="exports/attachments", null=True, blank=True)

class Order(models.Model):
    prod_name = models.CharField(max_length=250)
    quantity = models.BigIntegerField()
    export = models.ForeignKey(Export, on_delete=models.CASCADE)