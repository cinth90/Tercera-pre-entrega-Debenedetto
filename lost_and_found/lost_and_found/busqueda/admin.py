from django.contrib import admin
from django.utils import timezone
from .models import Ilost


# Register your models here.
from .models import *

class StaffAdmin(admin.ModelAdmin):
    list_display = ("what", "when", "where", "color")
    list_filter = ("what", "when", "where", "color")

class GuestAdmin(admin.ModelAdmin):
    list_display = ("what", "when", "where", "color")
    list_filter = ("what", "when", "where", "color")


    
admin.site.register(Ifound, StaffAdmin)
admin.site.register(Ilost, GuestAdmin)

