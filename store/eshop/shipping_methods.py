# eshop/shipping_methods.py

from oscar.apps.shipping.methods import Base
from oscar.core import prices
from decimal import Decimal as D
from .models import ShippingMethod

class DPDHomeDelivery(Base):
    code = 'dpd-home'
    name = 'DPD Home Delivery'

    def calculate(self, basket):
        try:
            method = ShippingMethod.objects.get(code=self.code)
            if method.is_active:
                charge = method.flat_rate
            else:
                charge = D('0.00')
        except ShippingMethod.DoesNotExist:
            charge = D('0.00')

        return prices.Price(
            currency=basket.currency,
            excl_tax=charge,
            incl_tax=charge
        )

class DPDPickup(Base):
    code = 'dpd-pickup'
    name = 'DPD Pickup Point'

    def calculate(self, basket):
        try:
            method = ShippingMethod.objects.get(code=self.code)
            if method.is_active:
                charge = method.flat_rate
            else:
                charge = D('0.00')
        except ShippingMethod.DoesNotExist:
            charge = D('0.00')

        return prices.Price(
            currency=basket.currency,
            excl_tax=charge,
            incl_tax=charge
        )
