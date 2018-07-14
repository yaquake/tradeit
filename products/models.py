from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=2000)
    pub_date = models.DateTimeField()
    body = models.TextField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default='Active')

    def __str__(self):
        return self.title


class Images(models.Model):
    item = models.OneToOneField(Product, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.item)


class Cart(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.master)


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

