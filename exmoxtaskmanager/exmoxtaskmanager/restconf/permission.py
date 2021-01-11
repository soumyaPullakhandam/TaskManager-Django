from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
       Object-level permission to only allow admin to create, update and delete it.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff


class IsAdminOrReadUpdateOnly(permissions.BasePermission):
    """
       Object-level permission to allow admin to do all actions.
       assigned user to read and update it.
       Assumes the model instance has an `user` attribute.
    """

    def has_object_permission(self, request, view, obj):

        user_allowed_methods = ['PATCH', 'GET']

        if request.user.is_staff:
            return True

        elif obj.user == request.user and request.method in user_allowed_methods:
            return True
