from django.urls import path
from exports.apis.views.create import create_export
from exports.apis.views.update import update_export
from exports.apis.views.delete import delete_export
from exports.apis.views.get import get_export, get_all

urlpatterns = [
    path("create/", create_export),
    path("update/<int:export_id>/", update_export),
    path("delete/<int:export_id>/", delete_export),
    path("get-all/", get_all),
    path("get/<int:export_id>/", get_export),
]