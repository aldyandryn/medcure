from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Item)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','date_added','amount', 'description', 'price')