# Django Library
from django.urls import path
from .views import SellBond, ListCustomerBond, BondManage

urlpatterns = [
    path('sale-bond/', SellBond.as_view(),
         name='sell_bond'),
    path('create-bond/', BondManage.as_view(), name='create_bond'),
    path('update-bond/<int:pk>/', BondManage.as_view(), name='update_bond'),
    path('list-bond/',ListCustomerBond.as_view(), name='list_bond')

]
