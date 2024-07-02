from django.urls import path
from .views.patients import get_patient_report, get_not_received_patients, get_received_patients
from .views.exports import get_exported_items, get_monthly_exports

urlpatterns = [
    path("inclusive-patient/<int:document_number>/", get_patient_report),
    path("received-patients/<str:date>/", get_received_patients),
    path("not-received-patients/<str:date>/", get_not_received_patients),

    path("check-exports/<str:date>/<str:sec_date>/", get_exported_items),
    path("get-monthly-exports/<str:date>/", get_monthly_exports),
]