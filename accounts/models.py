from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.TextField(max_length=70)
    address2 = models.TextField(max_length=50, blank=True)
    city = models.TextField(max_length=20)
    country = models.TextField(max_length=20)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/1.png')
    phone = models.TextField(max_length=15, default=True)
    postcode = models.IntegerField()

    def __str__(self):
        return "%s's profile" % self.user

