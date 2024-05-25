from django.urls import path
from exports.apis.views.create import create_export

urlpatterns = [
    path("create/", create_export)
]