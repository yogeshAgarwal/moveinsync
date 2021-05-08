
# Django Library
from datetime import date, datetime, time, timedelta
from django.utils import timezone
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Third Party Library
from django.contrib.auth.models import Permission
from bond_portfolio.models import Administrator, Customer, SalesPerson
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BondManageSerializers, SalesRecordSerializers
from .authentications import IsCustomer,IsAdministor,IsSalesPerson
from .models import Bond, BaseUser, SalesRecord

# Own Library

# Local Library


class BondManage(APIView):
    authentication_classes = [IsAdministor]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            data = request.data
        except Exception as e:
            print("[Error] BondManage",e)
            return Response({"msg":e},status=status.HTTP_400_BAD_REQUEST)
        updated_date = timezone.now()
        created_date = updated_date
        data['updated_date'] = updated_date
        data['created_date'] = created_date
        serilized_data = BondManageSerializers(data=data)
        if serilized_data.is_valid():
            serilized_data.save()
            return Response({"msg":"Bond Created Successfully"},status=status.HTTP_201_CREATED)
        return Response({"msg":serilized_data.errors},status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        data = request.data
        bond_ob = Bond.objects.get(id=pk)
        serilized_data = BondManageSerializers(bond_ob, data=data, partial=True)
        if serilized_data.is_valid():
            serilized_data.save()
            return Response({"msg":"Bond updated Successfully"},status=status.HTTP_201_CREATED)
        return Response({"msg":serilized_data.errors},status=status.HTTP_400_BAD_REQUEST)


class SellBond(APIView):
    authentication_classes = [IsSalesPerson, IsCustomer]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        if data.get('bond', None):
            id = data.get('bond', None)
            bond = Bond.objects.filter(id=id).first()
            if not bond:
                return Response({"msg":"bond should exist"},status=status.HTTP_400_BAD_REQUEST)
            else:
                data['bond'] = bond
        else:
            return Response({"msg":"bond is mandetory"},status=status.HTTP_400_BAD_REQUEST)
        user = getattr(request._request, 'user', None)
        if user.types == BaseUser.Types.SALES_PERSON:
            data['sales_person'] = user
            if data.get('customer', None):
                customer = data.get('customer', None)
                customer = Customer.objects.filter(username=customer).first()
                if not customer:
                    return Response({"msg":"Customer should be registered"},status=status.HTTP_400_BAD_REQUEST)
                else:
                    data['customer'] = customer
        elif user.types == BaseUser.Types.CUSTOMER:
            data['customer'] = user
            data['sales_person'] = None
        else:
            return Response({"msg":"User should be customer or Sales Person"},status=status.HTTP_400_BAD_REQUEST)
        created_date = timezone.now()
        data['created_date'] = created_date
        try:
            obj = SellBond(**data)
            obj.save()
            return Response({"msg":"successfull"},status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Exception",e)
            return Response({"msg":f"not created successfully {e}"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"msg":"successfull"},status=status.HTTP_201_CREATED)


class ListCustomerBond(APIView):
    authentication_classes = [IsCustomer]
    permission_classes = [IsAuthenticated]
    authentication_classes = []
    def post(self, request):
        data = request.data
        username = data.get('username',None)

        if not username:
            return Response({"msg":"Sales Record Created Successfully"},status=status.HTTP_400_BAD_REQUEST)

        customer = Customer.objects.filter(username=username)
        required_data = SalesRecord.objects.filter(customer=customer)
        serialized_data = SalesRecordSerializers(required_data, many=True)
        return Response({"data":serialized_data.data},status=status.HTTP_200_OK)