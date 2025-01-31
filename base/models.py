from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.


class CarouselImage(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    class Meta:
        verbose_name = "Carousel Image"
        verbose_name_plural = "Carousel Images"



class NewListing(models.Model):
    carousel = models.ForeignKey(CarouselImage, on_delete=models.CASCADE, related_name="carouselnewlisting")
    image =  models.ImageField(upload_to='newlisting', default='', blank=True, null=True)
    cloundImage =  CloudinaryField('Image', overwrite=True, format='jpg', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Meta:
        verbose_name = 'New Listing'
        verbose_name_plural = 'New Listing'


class OtherImages(models.Model):
    carousel = models.ForeignKey(CarouselImage, on_delete=models.CASCADE, related_name="carouselotherimages")
    image =  models.ImageField(upload_to='otherimages', default='', blank=True, null=True)
    cloundImage =  CloudinaryField('Image', overwrite=True, format='jpg', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Meta:
        verbose_name = 'Other Images'
        verbose_name_plural = 'Other Images'


class NewsLetter(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Meta:
        verbose_name = 'News Letter'
        verbose_name_plural = 'News Letters'



