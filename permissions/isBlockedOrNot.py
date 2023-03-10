from users.models import User
from rest_framework import permissions
from rest_framework.views import View
from rest_framework.exceptions import NotAcceptable


class IsBlockedOrNot(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        if request.user["is_blocked"] is True:
            return NotAcceptable("Account has been blocked")
