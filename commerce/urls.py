from django.urls import path
from . import views

app_name = "commerce"


urlpatterns=[
    path('category', views.categoryList, name='category'),
    path('tag/<slug:tag_slug>', views.categoryList, name='tags_by_tag'),
    path('product/<slug:category_slug>', views.prouctList, name='categories_by_category'),
    path('tag/<slug:tag_slug>', views.prouctList, name='tags_by_tag'),
    path('detail/<str:slug>', views.prodDetails, name='detail'),
    path('addtocart', views.addtocart, name='addtocart'),
    path('cart', views.cart, name='cart'),
    path('updatecart', views.updatecart, name='updatecart'),
    path('remove_item', views.remove_item, name='remove_item'),
]