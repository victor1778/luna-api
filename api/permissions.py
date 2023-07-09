from rest_framework import permissions
import uuid

class IsMessageOwner(permissions.BasePermission):
    message = "Editing or deleting messages is only allowed for the original user."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        
        print(str(uuid.UUID(request.user.id)))

        return str(obj.sender_id) == str(uuid.UUID(request.user.id))  