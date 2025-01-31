from django.db import models
from django.template.defaultfilters import slugify

from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField
from commerce.models import *

# Create your models here.


class ProductCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name="prods")
    quantity =models.IntegerField()
    name = models.CharField(max_length=100)
    total = models.IntegerField(default=1)
    order_no= models.CharField(max_length=50)
    session_id= models.CharField(max_length=100, blank= True, null= True)
    item_paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    class Meta:
        unique_together = ('order_no', 'session_id',)
        verbose_name_plural = "Carts"


class Checkout(models.Model):
    STATUS = [
    ('New','New'),
    ('Pending','Pending'),
    ('Processing','Processing'),
    ('Shipping','Shipping'),
    ('Delivered','Delivered'),
    ]
    firstname= models.CharField(max_length=50,blank=True, null=True,)
    lastname= models.CharField(max_length=50,blank=True, null=True,)
    email= models.EmailField(max_length=100, blank=True, null=True)
    address= models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    itm_paid= models.BooleanField(default=False)
    total= models.FloatField()
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    session_id= models.CharField(max_length=100, blank= True, null= True)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length = 50, choices=STATUS, blank=True, null=True)
    admin_remark= models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.firstname

    class Meta:
        verbose_name_plural = "Shipping Address"



class Paidorder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    total = models.FloatField()
    cart_no = models.CharField(max_length=36, blank=True, null=True)
    payment_code = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    paid_item = models.BooleanField(default=False)
    firstname= models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.name
    
    class Meta:
        verbose_name_plural = "Paid Orders"

    

class Ship(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    ordr_no= models.CharField(max_length=50)
    things_bought= models.CharField(max_length=500, blank=True, null=True)
    itm_paid= models.BooleanField(default=False)
    address= models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    total= models.FloatField()
    firstname= models.CharField(max_length=200,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

