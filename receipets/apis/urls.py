from django.urls import path
from .views.create import create_receipt
from .views.delete import delete_receipt
from .views.get import get_receipt, get_receipts
from .views.update import update_receipt

urlpatterns = [
    path("create/", create_receipt),
    path("get-receipts/", get_receipts),
    path("get/<int:receipt_id>/", get_receipt),
    path("delete/<int:receipt_id>/", delete_receipt),
    path("update/<int:receipt_id>/", update_receipt),
]