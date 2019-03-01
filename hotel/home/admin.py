from django.contrib import admin

# Register your models here.
from .models import Hotels, City

admin.site.register(Hotels)
admin.site.register(City)
