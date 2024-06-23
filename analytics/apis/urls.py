from django.urls import path
from .views.exports import get_exports
from .views.receipts import get_receipts
from .views.patients import get_patients

urlpatterns = [
    path("get-exports/", get_exports),
    path("get-receipts/", get_receipts),
    path("get-patients/", get_patients),
]