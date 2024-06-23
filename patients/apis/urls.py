from django.urls import path
from .views.create import create_patient
from .views.update import update_patient
from .views.delete import delete_patient
from .views.search import search_patients
from .views.get import get_patient, get_all

urlpatterns = [
    path("create/", create_patient),
    path("update/<int:patient_id>/", update_patient),
    path("delete/<int:patient_id>/", delete_patient),
    path("get/<int:paitent_id>/", get_patient),
    path("search/<int:doc_num>/", search_patients),
    path("get-all/", get_all),
]