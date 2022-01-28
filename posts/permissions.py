from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # SAFE_METHODS - get, option, head
            return True
        return obj.author == request.user


class IsAuthorOrAdminDeleteOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'DELETE' and request.user.is_superuser:
            return True
        return obj.author == request.user


class NotPostman(permissions.BasePermission):
    message = 'Postman not allowed'

    def has_permission(self, request, view):
        user_agent = request.META['HTTP_USER_AGENT']
        return 'Postman' not in user_agent
