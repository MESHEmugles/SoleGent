from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(ProductCart)
class ProductCartAdmin(admin.ModelAdmin):
    list_display_links = ('product',)
    search_fields = ('name','product')
    list_display = ("product","created")


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display_links = ('firstname',)
    search_fields = ('firstname','email')
    list_display = ("firstname","created")


@admin.register(Paidorder)
class PaidorderAdmin(admin.ModelAdmin):
    list_display_links = ('product',)
    search_fields = ('cart_no','payment_code')
    list_display = ("product","created")


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display_links = ('product',)
    search_fields = ('ordr_no','product')
    list_display = ("product","created")
