from django.contrib import admin
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)