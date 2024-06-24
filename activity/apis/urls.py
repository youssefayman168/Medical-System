from django.urls import path
from .views.get import get_activities
from .views.update import read_activity, read_all

urlpatterns = [
    path("get/", get_activities),
    path("read/<int:activity_id>/", read_activity),
    path("read-all/", read_all),
]