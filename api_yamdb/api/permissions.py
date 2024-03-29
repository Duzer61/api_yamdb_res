from rest_framework import permissions


class isModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return self.action 


class isAdministrator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class isSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class IsOwnerOrModeratorOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        return (obj.author == request.user
                or request.user.is_moderator
                or request.user.is_admin)


class isAdministratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user.is_authenticated and (request.user.is_admin
                or request.user.is_staff))
