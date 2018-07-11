from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=2000)
    pub_date = models.DateTimeField()
    body = models.TextField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=25, default=True)
    subcategory = models.CharField(max_length=25, default=True)
    status = models.CharField(max_length=30, default='Active')

    def __str__(self):
        return self.title


class Images(models.Model):
    item = models.OneToOneField(Product, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    image4 = models.ImageField(upload_to='images/')
    image5 = models.ImageField(upload_to='images/')


class Cart(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.OneToOneField(Product, on_delete=models.CASCADE)


