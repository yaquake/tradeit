
from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('info/', include('info.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
