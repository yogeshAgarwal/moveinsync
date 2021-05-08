from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import ForeignKey
# from django.db.models.fields import proxy
from django.utils.translation import gettext_lazy as _

class BaseUser(AbstractUser):

    class Types(models.TextChoices):
        ADMINISTRATOR = "ADMINISTRATOR", "Administrator"
        SALES_PERSON = "SALES_PERSON", "Sales Person"
        CUSTOMER = "CUSTOMER", "Customer"

    types = models.CharField(_('Types'), max_length=100,choices=Types.choices,null=False, blank=False)
    name = models.CharField(_('Name of User'), max_length=200)

    def __str__(self) -> str:
        return super().__str__()

class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(types=BaseUser.Types.CUSTOMER)



class SalesPersonManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(types=BaseUser.Types.SALES_PERSON)




class AdministratorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(types=BaseUser.Types.ADMINISTRATOR)




class Customer(BaseUser):
    objects = CustomerManager()

    class Meta:
        proxy = True
        permissions = []

    def save(self, *args, **kwargs):
        if not self.pk:
            self.types = BaseUser.Types.CUSTOMER
        return super().save(*args, **kwargs)

class SalesPerson(BaseUser):
    objects = SalesPersonManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.types = BaseUser.Types.SALES_PERSON
        return super().save(*args, **kwargs)

class Administrator(BaseUser):
    objects = AdministratorManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.types = BaseUser.Types.ADMINISTRATOR
        return super().save(*args, **kwargs)

class Bond(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    pricing = models.FloatField(null=False)
    avg_return = models.FloatField(null=False)
    current_profit_predition = models.FloatField(null=False)
    updated_date = models.DateTimeField()
    created_date = models.DateTimeField()


class SalesRecord(models.Model):
    bond = models.ForeignKey(Bond, on_delete=DO_NOTHING)
    sales_person = models.ForeignKey(SalesPerson, on_delete=DO_NOTHING,
                                        related_name='sales_person',null=True)
    customer = models.ForeignKey(Customer, on_delete=DO_NOTHING)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField()