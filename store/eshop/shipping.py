from oscar.apps.shipping import repository
from oscar.apps.shipping.methods import Free, NoShippingRequired
from .shipping_methods import DPDHomeDelivery, DPDPickup

class CustomShippingRepository(repository.Repository):

    def get_available_shipping_methods(self, basket, shipping_addr=None, **kwargs):
        methods = [
            DPDHomeDelivery(),
            DPDPickup(),
            Free(),
        ]

        if basket.is_shipping_required():
            return methods
        else:
            return [NoShippingRequired()]
