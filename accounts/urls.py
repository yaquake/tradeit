from django.urls import path, include
from . import views

urlpatterns = [
    path('registration', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('profile', views.userprofile, name='profile'),
    path('<str:uploader>', views.seller, name='seller'),
]