from django.db import models
from django.utils import timezone 
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


#Valida que la fecha no sea en el futuro
def validate_past_date(value):
        if value > timezone.now().date():
            raise ValidationError(
            _('The date must be today or earlier')
        )
#Valida que el numero de cuarto sea real
def validate_four_digits(value):
    if not (1101 <= value <= 3510):
        raise ValidationError(
            _('%(value)s room number not valid'),
            params={'value': value},)


#Modelo Ilost(objeto perdido)
class Ilost(models.Model):
        LOCATIONS = [
                    ("Lobby", "Lobby"),
                     ("Tonic bar", "Tonic bar"),
                     ("Graze: Breakfast", "Graze: Breakfast"),
                     ("Underwater Observatory", "Underwater Observatory"),
                     ("North end Pool", "North end Pool"),
                     ("Salti: Restaurant", "Salti: Restaurant"),
                     ("Infinity: Restaurant", "Infinity: Restaurant"),
                     ("Kid's club", "Kid's club"),
                     ("Living reef center", "Living reef center"),
                     ("The Shake/Candy shop", "The Shake/Candy shop"),
                     ("Canopy wing: corridor", "Canopy wing: corridor"),
                     ("Driftwood wing: corridor", "Driftwood wing: corridor"),
                     ("Harbour wing: corridor", "Harbour wing: corridor"),
                     ("Transit Lounge", "Transit Lounge"),
                     ("Ferry", "Ferry"),        
                     ("South end pool", "South end pool"),
                     ("Water sports", "Water sports"),
                     ("My room", "My room"),
                     ("Lover's Cove", "Lover's Cove"),
                     ("Rain forest walk", "Rain forest walk"),
                     ("Tennis/Basquet court", "Tennis/Basquet court"),
                     ("I don't know", "I don't know"),
    ]
        name_booking = models.CharField(max_length=60, blank=False, null=False, default='')
        room_number = models.IntegerField(validators=[validate_four_digits], blank=True, null=True)
        email= models.EmailField(max_length=254, blank=False, null=False, default='')
        when = models.DateField(validators=[validate_past_date])
        what = models.CharField(max_length=60)
        where = models.CharField(max_length=60, choices=LOCATIONS, help_text="Select a place where you lost your item")
        color = models.CharField(max_length=50, blank=True, null=True)
        model = models.CharField(max_length=60, blank=True, null=True)
        size = models.CharField(max_length=60, blank=True, null=True)
        description = models.TextField(verbose_name="Description", help_text="Optional: Complete a short description of item", blank=True, null=True)
        photo = models.ImageField(upload_to='lost_photos/', blank=True, null=True, help_text='Opcional: load a photo of the item')
        returned_owner = models.BooleanField(default=False)
    
        def __str__(self):
            return f"{self.what}"
    
        class Meta:
            verbose_name = "Lost Property"
            verbose_name_plural = "Lost Properties"
            ordering = ["when", "what"]




#Modelo IFound(obejto encontrado)
class Ifound(models.Model):
        LOCATIONS = [
                    ("Lobby", "Lobby"),
                     ("Tonic bar", "Tonic bar"),
                     ("Graze: Breakfast", "Graze: Breakfast"),
                     ("Underwater Observatory", "Underwater Observatory"),
                     ("North end Pool", "North end Pool"),
                     ("Salti: Restaurant", "Salti: Restaurant"),
                     ("Infinity: Restaurant", "Infinity: Restaurant"),
                     ("Kid's club", "Kid's club"),
                     ("Living reef center", "Living reef center"),
                     ("The Shake/Candy shop", "The Shake/Candy shop"),
                     ("Canopy wing: corridor", "Canopy wing: corridor"),
                     ("Driftwood wing: corridor", "Driftwood wing: corridor"),
                     ("Harbour wing: corridor", "Harbour wing: corridor"),
                     ("Transit Lounge", "Transit Lounge"),
                     ("Ferry", "Ferry"),        
                     ("South end pool", "South end pool"),
                     ("Water sports", "Water sports"),
                     ("My room", "My room"),
                     ("Lover's Cove", "Lover's Cove"),
                     ("Rain forest walk", "Rain forest walk"),
                     ("Tennis/Basquet court", "Tennis/Basquet court"),
                     ("I don't know", "I don't know"),
    ]
        
        when = models.DateField(validators=[validate_past_date])
        what = models.CharField(max_length=60)
        where = models.CharField(max_length=60, choices=LOCATIONS, help_text="Select a place where you lost your item")
        color = models.CharField(max_length=50)
        model = models.CharField(max_length=60)
        size = models.CharField(max_length=60)
        description = models.TextField(verbose_name="Description", help_text="Optional: Complete a short description of item", blank=True, null=True)
        photo = models.ImageField(upload_to='found_photos/', blank=True, null=True, help_text='Opcional: load a photo of the item')
        returned_owner = models.BooleanField(default=False)
        
        def __str__(self):
            return f"{self.what}"
        
        class Meta:
            verbose_name = "Found Property"
            verbose_name_plural = "Found Properties"
            ordering = ["when", "what"]

#Modelo Testimonials (Reseña de los huspedes que usaron el servicio)

class Testimonial(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    testimonial = models.TextField(max_length=900)

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.city}"
   
#Avatar
   
class Avatar(models.Model):
    imagen = models.ImageField(upload_to= "avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE) #BORRA LOS AVATARES QUE YA NO ESTAN EN USO
    
    def __str__(self):
        return f"{self.user} {self.imagen}"

# Formulario de contacto    
class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=15, default='')
    message = models.TextField(default='')

    def __str__(self):
        return self.name