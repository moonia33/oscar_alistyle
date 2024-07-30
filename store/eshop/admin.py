# eshop/admin.py

from django.contrib import admin
from .models import ShippingMethod

@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active', 'flat_rate')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')
