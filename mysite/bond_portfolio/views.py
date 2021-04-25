
# Django Library


# Third Party Library
from django.contrib.auth.models import Permission
from bond_portfolio.models import Administrator, Customer, SalesPerson
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BondManageSerializers, SalesRecordSerializers
from .authentications import SalesPersonPermission, AdministatorPermission, CustomerPermission

# Own Library

# Local Library


class BondManage(APIView):
    permission_classes = [AdministatorPermission]
    def post(self, request):
        data = request.data
        serilized_data = BondManageSerializers(data=data, many=True)
        if serilized_data.is_valid():
            serilized_data.save()
            return Response({"msg":"Bond Created Successfully"},status=status.HTTP_201_CREATED)
        return Response({"msg":serilized_data.errors},status=status.HTTP_201_CREATED)


    def patch(self, request, pk):
        data = request.data
        serilized_data = BondManageSerializers(data=data, many=True, partial=True)
        if serilized_data.is_valid():
            return Response({"msg":"Bond Created Successfully"},status=status.HTTP_201_CREATED)


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