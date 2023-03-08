# from rest_framework import permissions
# from rest_framework.views import Request, View
# from books.models import Book
# class IsBookOwnerOrAdmin(permissions.BasePermission):
#     def has_object_permission(self, request:Request, view:View, obj:Book):
#         return request.user.is_superuser or request.user == obj.user_followers
