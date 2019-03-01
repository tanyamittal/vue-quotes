from django.contrib import admin
from .models import Hotel,Booking,Room,User
# Register your models here.
admin.site.register(Hotel)
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Booking)
