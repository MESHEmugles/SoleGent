from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('product/<slug:category_slug>/', index, name='categories_by_category'),
    path('about/', about, name='aboutus'),
    path('contact/', contact, name='contact'),
    path('subscribe/', save_email, name='save_email')
]
