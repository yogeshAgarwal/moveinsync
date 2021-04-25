# Django Library
from django.urls import path
from .views import SellBond, BuyBond, BondManage

urlpatterns = [
    path('sales-bond/', SellBond.as_view(),
         name='sell_bond'),
    path('manage-bond/', BondManage.as_view(), name='manage_bond')

]
