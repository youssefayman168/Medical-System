from django.urls import path, include
from .views.create import create_user
from .views.delete import delete_user
from .views.get import get_user, get_users
from .views.update import update_user
from .views.login import login
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("create/", create_user),
    path("delete/<int:user_id>/", delete_user),
    path("update/<int:user_id>/", update_user),
    path("get-user/<int:user_id>/", get_user),
    path("get/", get_users),
    path("login/", login),
    # path('reset-password/', include("users.apis.views.reset_password.urls")),
    path("refresh/", TokenRefreshView.as_view())
]