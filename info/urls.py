from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('payment', views.payment, name='payment'),
]