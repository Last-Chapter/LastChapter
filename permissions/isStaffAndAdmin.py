from rest_framework import permissions
from users.models import User
from rest_framework.views import View


class IsStaffAndAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        return request.user.is_authenticated and request.user.is_admin
