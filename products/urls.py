from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:product_id>', views.details, name='details'),
    path('cart', views.cart, name='cart'),
    path('addtocart/<int:product_id>', views.addtocart, name='addtocart'),
    # path('admindetails/<int:product_id>', views.admindetails, name='admindetails'),
    path('changedetails/<int:product_id>', views.changedetails, name='changedetails'),
    path('delete/<int:product_id>', views.delete, name='delete'),
    path('productlist', views.productlist, name='productlist'),
    path('deletefromcart/<int:product_id>', views.deletefromcart, name='deletefromcart'),
    path('search', views.search, name='search'),
    path('buy', views.buy, name='buy'),
]