from django.urls import path
from . import views

app_name = "productcart"


urlpatterns=[
    path('', views.checkout, name='checkout'),
    path('paidorder/', views.paidorder, name='paidorder'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('on-delivery/', views.nocardthankyou, name='nocardthankyou'),
]