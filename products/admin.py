from django.contrib import admin
from django.utils.html import format_html
from django.template.defaultfilters import escape
from django.urls import reverse

# Register your models here.
from .models import Product
from .models import Images
from .models import Category
from .models import Cart
from django.contrib.auth.models import User


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploader', 'pub_date', 'images')

    def uploader(self, obj):
        return obj.uploader.username

    def images(self, obj):
        return str(obj.image1.url)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'uploader')
    list_display_links = ('item_id', 'uploader')

    def item_id(self, obj):
        return obj.item.id

    def uploader(self, obj):
        return obj.item.uploader.username


admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Category)
admin.site.register(Cart)