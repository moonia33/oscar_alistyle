# apps/partner/strategy.py

from oscar.apps.partner.strategy import UseFirstStockRecord, StockRequired, FixedRateTax, Structured, Selector
from collections import namedtuple
from decimal import Decimal as D


class Selector(object):
    """
    Responsible for returning the appropriate strategy class for a given
    user/session.

    This can be called in three ways:

    #) Passing a request and user. This is for determining
       prices/availability for a normal user browsing the site.

    #) Passing just the user. This is for offline processes that don't
       have a request instance but do know which user to determine prices for.

    #) Passing nothing. This is for offline processes that don't
       correspond to a specific user, e.g., determining a price to store in
       a search index.

    """

    # pylint: disable=unused-argument
    def strategy(self, request=None, user=None, **kwargs):
        """
        Return an instantiated strategy instance
        """
        # Default to the backwards-compatible strategy of picking the first
        # stockrecord but charging zero tax.
        return LitTax(request)


# pylint: disable=unused-argument


class LitTax(UseFirstStockRecord, StockRequired, FixedRateTax, Structured):
    rate = D("0.21")

