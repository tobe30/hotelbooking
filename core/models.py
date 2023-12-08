from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural ='Categories'

    def __str__(self):
        return self.name
    
class rooms(models.Model):
    rid = ShortUUIDField(unique=True, length=10, max_length=20,  alphabet="abc123")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, related_name='book', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_images', blank=True, null=True)
    price = models.DecimalField(max_digits=99999999999999, decimal_places=0, default="1.99")
    adult = models.IntegerField(default=0)
    children = models.IntegerField(default=0)
    amenities = models.CharField(max_length=100, default="Wifi")
    beds = models.CharField(max_length=10, default="2(double)")
    description = models.TextField(blank=True, null=True)
    available =models.BooleanField(default=True)
    unavailable =models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='book', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name_plural = "rooms"

    def room_Image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

class Amenities(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='book_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Booking(models.Model):
    category = models.CharField(max_length=255, null=True, blank=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200) # +234 (456) - 789
    email = models.CharField(max_length=200)
    adult = models.IntegerField(default=0)
    children = models.IntegerField(default=0)
    checkin =  models.DateTimeField(null=True)
    checkout =  models.DateTimeField(null=True)
    request = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Booking"

    def __str__(self):
        return self.firstname