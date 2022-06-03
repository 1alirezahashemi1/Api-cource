from rest_framework.permissions import *

# Write Your Permissions Here !

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_superuser
        )

class IsStafforReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool (
            request.method in SAFE_METHODS or
            request.user and request.user.is_authenticated 
        )

class IssuperUserOrStaffreadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS  and request.user.is_staff or
            request.user and request.user.is_superuser
            
        )

class IsAuthororReadonly(BasePermission):
    def has_object_permission(self, request, view,obj):        
            if request.method  in SAFE_METHODS: 
                return True
            
            return bool(
                    request.user.is_authenticated and request.user.is_superuser or
                    request.user.is_authenticated and obj.author == request.user

                    
            )

     
