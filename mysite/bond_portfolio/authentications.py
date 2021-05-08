# Django Library

# Third Party Library
from rest_framework.permissions import BasePermission
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import BaseUser



class AdministatorPermission(BasePermission):

    message = "Access Denied"

    def has_permission(self, request, view):
        username = request.data.get('username', None)
        user_ob = BaseUser.objects.filter(username=username).first()
        if user_ob:
            if user_ob.types == BaseUser.Types.ADMINISTRATOR:
                return True
        return False


class SalesPersonPermission(BasePermission):

    message = "Access Denied"

    def has_permission(self, request, view):
        username = request.data.get('username', None)
        user_ob = BaseUser.objects.filter(username=username).first()
        if user_ob:
            if user_ob.types == BaseUser.Types.SALES_PERSON:
                return True
        return False

class CustomerPermission(BasePermission):

    message = "Access Denied"

    def has_permission(self, request, view):
        username = request.data.get('username', None)
        user_ob = BaseUser.objects.filter(username=username).first()
        if user_ob:
            if user_ob.types == BaseUser.Types.CUSTOMER:
                return True
        return False

class IsAdministor(SessionAuthentication):
    def authenticate(self, request):
        user = getattr(request._request, 'user', None)
        # Unauthenticated, CSRF validation not required
        if not user or not user.is_active or not user.types == BaseUser.Types.ADMINISTRATOR:
            return None
        super().enforce_csrf(request)
        # CSRF passed with authenticated user
        return (user, None)

class IsCustomer(SessionAuthentication):
    def authenticate(self, request):
        user = getattr(request._request, 'user', None)
        # Unauthenticated, CSRF validation not required
        if not user or not user.is_active or not user.types == BaseUser.Types.CUSTOMER:
            return None
        super().enforce_csrf(request)
        # CSRF passed with authenticated user
        return (user, None)

class IsSalesPerson(SessionAuthentication):
    def authenticate(self, request):
        user = getattr(request._request, 'user', None)
        # Unauthenticated, CSRF validation not required
        if not user or not user.is_active or not user.types == BaseUser.Types.SALES_PERSON:
            return None
        self.super().enforce_csrf(request)
        # CSRF passed with authenticated user
        return (user, None)
