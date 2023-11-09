from rest_framework.permissions import BasePermission, IsAuthenticated

from users.models import UserRoles

class IsOwner(IsAuthenticated):
    message = "Необходимо иметь права владельца."

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False

class IsModerator(IsAuthenticated):
    message = "Необходимо иметь права модератора."

    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        return is_authenticated and request.user.groups.filter(name='moderator').exists()

#    def has_permission(self, request, view):
#        if request.user.role == UserRoles.MODERATOR:
#            return True
#        return False