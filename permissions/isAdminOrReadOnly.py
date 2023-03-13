from rest_framework import permissions
from rest_framework.views import View


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view: View):
        if request.method == "POST":
            return request.user.is_superuser 
        return True
        
