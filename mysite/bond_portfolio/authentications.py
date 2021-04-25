# Django Library

# Third Party Library
from rest_framework.permissions import BasePermission
from .models import BaseUser



class AdministatorPermission(BasePermission):

    message = "Access Denied"

    def has_permission(self, request, view):
        access_user_id = request.data.get('user_id', None)
        user_ob = BaseUser.objects.filter(id=access_user_id)
        if user_ob:
            if user_ob.types == BaseUser.Types.ADMINISTRATOR:
                return True
        return False


class SalesPersonPermission(BasePermission):

    message = "Access Denied"

    def has_permission(self, request, view):
        access_user_id = request.data.get('user_id', None)
        user_ob = BaseUser.objects.filter(id=access_user_id)
        if user_ob:
            if user_ob.types == BaseUser.Types.SALES_PERSON:
                return True
        return False

class CustomerPermission(BasePermission):

    message = "Access Denied"

    def has_permission(self, request, view):
        access_user_id = request.data.get('user_id', None)
        user_ob = BaseUser.objects.filter(id=access_user_id)
        if user_ob:
            if user_ob.types == BaseUser.Types.CUSTOMER:
                return True
        return False