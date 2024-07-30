# store/apps/shipping/repository.py

from oscar.apps.shipping import repository
from oscar.core import prices
from .methods import DPDPickup, DPDHomeDelivery
from oscar.apps.shipping.repository import Repository as CoreRepository
from decimal import Decimal as D



class CustomShippingRepository(repository.Repository):

    def get_available_shipping_methods(self, basket, shipping_addr=None, **kwargs):
        methods = [
            DPDPickup(),
            DPDHomeDelivery(),
        ]

        # Filtruoti metodus, kurie yra prieinami
        available_methods = [method for method in methods if method.is_available_to_user(basket)]

        # Rūšiuoti pagal kainą didėjančia tvarka (mažiausia kaina pirma)
        sorted_methods = self.sort_shipping_methods(available_methods, basket)

        # Nustatyti numatytąjį metodą (pirmas sąraše)
        default_method = sorted_methods[0] if sorted_methods else None

        return sorted_methods, default_method

    def sort_shipping_methods(self, methods, basket):
        # Rūšiuoti metodus pagal kainą mažėjančia tvarka (reverse=False)
        return sorted(methods, key=lambda method: method.calculate(basket).incl_tax, reverse=False)
        
class Repository(CoreRepository):
    methods = (DPDPickup(), DPDHomeDelivery(),)
