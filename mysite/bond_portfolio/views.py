
# Django Library
from datetime import date, datetime, time, timedelta
from django.utils import timezone

# Third Party Library
from django.contrib.auth.models import Permission
from bond_portfolio.models import Administrator, Customer, SalesPerson
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BondManageSerializers, SalesRecordSerializers
from .authentications import SalesPersonPermission, AdministatorPermission, CustomerPermission
from .models import Bond

# Own Library

# Local Library


class BondManage(APIView):
    permission_classes = [AdministatorPermission]
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
    permission_classes = [SalesPersonPermission]
    def post(self, request):
        data = request.data
        serilized_data = SalesRecordSerializers(data=data, many=True)
        if serilized_data.is_valid():
            serilized_data.save()
            return Response({"msg":"Sales Record Created Successfully"},status=status.HTTP_201_CREATED)
        return Response({"msg":serilized_data.errors},status=status.HTTP_201_CREATED)


class BuyBond(APIView):
    permission_classes = [CustomerPermission]
    def post(self, request):
        data = request.data
        serilized_data = SalesRecordSerializers(data=data, many=True)
        if serilized_data.is_valid():
            serilized_data.save()
            return Response({"msg":"Sales Record Created Successfully"},status=status.HTTP_201_CREATED)
        return Response({"msg":serilized_data.errors},status=status.HTTP_201_CREATED)