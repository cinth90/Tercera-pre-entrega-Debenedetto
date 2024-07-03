from django.db import models
from django.utils import timezone 
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

#Valida que la fecha no sea en el futuro
def validate_past_date(value):
        if value > timezone.now().date():
            raise ValidationError(
            _('La fecha no puede estar en el futuro.')
        )

#Modelo Ilost(objeto perdido)
class Ilost(models.Model):
    when = models.DateField(validators=[validate_past_date])
    what = models.CharField(max_length=60)
    where = models.CharField(max_length=60)
    color = models.CharField(max_length=50)
    model = models.CharField(max_length=60)
    size = models.CharField(max_length=60)
    return_owner = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.what}"
    
    class Meta:
        verbose_name = "Lost Property"
        verbose_name_plural = "Lost Properties"
        ordering = ["when", "what"]




#Modelo IFound(obejto encontrado)
class Ifound(models.Model):
    when = models.DateField(validators=[validate_past_date])
    what = models.CharField(max_length=60)
    where = models.CharField(max_length=60)
    color = models.CharField(max_length=50)
    model = models.CharField(max_length=60)
    size = models.CharField(max_length=60)
    return_owner = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.what}"
    
        
    class Meta:
        verbose_name = "Found Property"
        verbose_name_plural = "Found Properties"
        ordering = ["when", "what"]

#Modelo Testimonials (Reseña de los huspedes que usaron el servicio)

class Testimonial(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    testimonio = models.CharField(max_length=900)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.ciudad}"