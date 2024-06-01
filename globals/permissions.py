from rest_framework import permissions


class OnlyAdmins(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        
        return request.user.is_admin
    