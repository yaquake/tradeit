from django.urls import path, include
from . import views

urlpatterns = [
    path('registration', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('profile/<int:user_id>', views.userprofile, name='userprofile'),
    path('myprofile', views.myprofile, name='myprofile'),
    # path('<str:uploader>', views.seller, name='seller'),
    path('odmen', views.odmen, name='odmen'),
]