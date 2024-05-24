from django.db import models
from patients.models import Paitent

# Create your models here.
class Receipet(models.Model):
    patient = models.ForeignKey(Paitent, on_delete=models.CASCADE)
    receiving_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)