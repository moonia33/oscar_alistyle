from decimal import Decimal as D
from oscar.apps.shipping import methods
from django.utils.translation import gettext_lazy as _

from oscar.core import prices


        
class DPDPickup():
    code = 'dpd-pickup'
    name = 'DPD Pickup Point'
    is_discounted = False

    def calculate(self, basket):
        # Apskaičiuokite pristatymo kainą, pvz., 3.99 EUR
        charge_incl_tax = D('3.99')
        charge_excl_tax = D('3.30')  # Jei PVM nėra, tada abi reikšmės yra vienodos

        return prices.Price(
            currency=basket.currency,
            excl_tax=charge_excl_tax,
            incl_tax=charge_incl_tax
        )
        
class DPDHomeDelivery():
    code = 'dpd-home'
    name = 'DPD Home Delivery'
    is_discounted = False

    def calculate(self, basket):
        total_quantity = sum(line.quantity for line in basket.lines.all())
        if total_quantity <= 5:
            charge = D('4.99')
        elif total_quantity <= 10:
            charge = D('7.99')
        else:
            charge = D('10.99')
        
        return prices.Price(
            currency=basket.currency,
            excl_tax=charge,
            incl_tax=charge
        )        