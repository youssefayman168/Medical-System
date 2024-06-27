from django.urls import path
from .views.patients import get_patient_report, get_not_received_patients, get_received_patients

urlpatterns = [
    path("inclusive-patient/", get_patient_report),
    path("received-patients/", get_received_patients),
    path("not-received-patients/", get_not_received_patients),
]