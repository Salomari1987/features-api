from rest_framework.permissions import BasePermission
from .models import Feature


class IsOwnerOrStaff(BasePermission):
    """Custom permission class to allow only features owners or admins to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the feature owner or user is staff/superuser."""
        if request.user.is_staff:
            return True
        elif isinstance(obj, Feature):
            return obj.owner == request.user
        return obj.owner == request.user
