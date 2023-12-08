from django.contrib import admin
from core.models import rooms, Category, Amenities, Booking

# Register your models here.
class roomsAdmin(admin.TabularInline):
    model = rooms

class roomsAdmin(admin.ModelAdmin):
    list_display = ['user', 'room_Image', 'price', 'adult', 'children', 'category','available', 'created_at', 'rid']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'email', 'adult', 'children', 'checkin', 'checkout', 'request']


admin.site.register(rooms, roomsAdmin)
admin.site.register(Category)
admin.site.register(Amenities)
admin.site.register(Booking, BookingAdmin)


