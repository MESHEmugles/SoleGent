from django.contrib import admin
from .models import *

# Register your models here.

class NewListingInline(admin.TabularInline):
    model = NewListing
    
class OtherImagesInline(admin.TabularInline):
    model = OtherImages
    

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ("created",)
    inlines = [NewListingInline, OtherImagesInline]



@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ("email", "created")

