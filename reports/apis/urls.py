from django.urls import path
from .views.patients import get_patient_report

urlpatterns = [
    path("inclusive-patient/", get_patient_report),
]