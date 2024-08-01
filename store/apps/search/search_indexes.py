from oscar.apps.search import ProductIndex as OscarProductIndex

class ProductIndex(OscarProductIndex):

    dydis = indexes.CharField(null=True, faceted=True)
    gamintojas = indexes.CharField(null=True, faceted=True)

    def prepare_dydis(self, obj):
        return obj.attribute_values.get(attribute__code="dydis").value_text

    def prepare_gamintojas(self, obj):
        return obj.attribute_values.get(attribute__code="gamintojas").value_text