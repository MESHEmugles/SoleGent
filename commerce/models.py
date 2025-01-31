from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    name =  models.CharField(max_length=50, null=True, blank=True)
    slug =  models.SlugField(unique=True)
    image =  models.ImageField(upload_to= 'category', default='', blank=True, null=True)
    cloundImage =  CloudinaryField('Image', overwrite= True, format= 'jpg', blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)


    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pages/product.html', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    @property
    def get_image(self):
        if self.image is None:
            return self.cloundImage 
        else:
            return self.image
    
    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=70, null=True, blank= True)
    slug =  models.SlugField(unique=True)
    image =  models.ImageField(upload_to= 'product', default='', blank=True, null=True)
    cloundImage =  CloudinaryField('Image', overwrite= True, format= 'jpg', blank=True, null=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="cats")
    des= CKEditor5Field('Text', config_name='default', null=True)
    min_order = models.IntegerField(default=1)
    max_order = models.IntegerField(default=5)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    oldprice = models.DecimalField(max_digits=10, decimal_places=2)
    available= models.BooleanField()
    overview= CKEditor5Field('Text', config_name='default', null=True)
    display = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('', kwargs=(self.slug))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    @property
    def get_image(self):
        if self.image is None:
            return self.cloundImage 
        else:
            return self.image
        
    def to_cart_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'price': float(self.price),
            'image': self.image.url if self.image else '',
            'category': self.category.name if self.category else '',
        }
    
    class Meta:
        verbose_name_plural = "Products"


