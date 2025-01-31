from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    search_fields = ('name',)
    list_display = ("name","created", "updated")
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    search_fields = ('name',"category","price","available",)
    list_display = ("name","category","price","created", "updated")
    prepopulated_fields = {'slug': ('name',)}