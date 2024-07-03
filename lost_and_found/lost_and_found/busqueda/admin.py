from django.contrib import admin
from django.utils import timezone
from .models import Ilost


# Register your models here.
from .models import *

class StaffAdmin(admin.ModelAdmin):
    list_display = ("what", "when", "where", "color") # Campos a mostrar en la lista
    list_filter = ("what", "when", "where", "color") # Campos para filtrar

class GuestAdmin(admin.ModelAdmin):
    list_display = ("what", "when", "where", "color") # Campos a mostrar en la lista
    list_filter = ("what", "when", "where", "color") # Campos para filtrar
    
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'ciudad')  # Campos a mostrar en la lista
    search_fields = ('nombre', 'apellido', 'ciudad')  # Campos para búsqueda


    
admin.site.register(Ifound, StaffAdmin)
admin.site.register(Ilost, GuestAdmin)
admin.site.register(Testimonial)

