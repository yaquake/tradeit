from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:product_id>', views.details, name='details'),
    path('cart', views.cart, name='cart'),
    path('addtocart/<int:product_id>', views.addtocart, name='addtocart'),
]