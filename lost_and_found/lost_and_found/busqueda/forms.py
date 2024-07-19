from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _
from django.utils import timezone 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

#Valida que la fecha no sea en el futuro
def validate_past_date(value):
        if value > timezone.now().date():
            raise ValidationError(
            _('The date must be today or earlier')
        )

    #Formulario para items perdidos
def validate_four_digits(value):
    if not (1101 <= value <= 3510):
        raise ValidationError(
            _('%(value)s room number not valid'),
            params={'value': value},
        )


class LostForm(forms.Form):
    LOCATIONS = [("Lobby", "Lobby"),
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
                 ("I don't know", "I don't know"),]
    name_booking = forms.CharField(max_length=60)
    room_number = forms.IntegerField(validators=[validate_four_digits])
    email= forms.EmailField(max_length=254)
    when = forms.DateField(validators=[validate_past_date], input_formats=['%d/%m/%Y'],widget=forms.DateInput(format='%d/%m/%Y'), required=True, help_text='Format: dd/mm/aaaa', error_messages= {'required': 'Complete date'})
    what = forms.CharField(max_length=20)
    where = forms.ChoiceField(choices=LOCATIONS, help_text='Select an option')
    color = forms.CharField(max_length=50, required=False, help_text='Optional: Complete color of item')
    model = forms.CharField(max_length=60, required=False, help_text='Optional: Complete model of item')
    size = forms.CharField(max_length=60, required=False, help_text='Optional: Complete size of item')
    description = forms.CharField(widget=forms.Textarea, required=False, help_text='Optional: Complete a short description of item')
    photo = forms.ImageField(required=False, help_text='Opcional: load a photo of the item')

    
class FoundForm(forms.Form):
    LOCATIONS = [("Lobby", "Lobby"),
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
                 ("I don't know", "I don't know"),]
    when = forms.DateField(widget=forms.DateInput(attrs={'id': 'id_when'}), input_formats=['%d/%m/%Y'], required=True, help_text='Format: dd/mm/aaaa', error_messages= {'required': 'Complete date'})
    what = forms.CharField(max_length=20)
    where = forms.ChoiceField(choices=LOCATIONS, help_text='Select an option')
    color = forms.CharField(max_length=50, required=False, help_text='Optional: Complete color of item')
    model = forms.CharField(max_length=60, required=False, help_text='Optional: Complete model of item')
    size = forms.CharField(max_length=60, required=False, help_text='Optional: Complete size of item')
    description = forms.CharField(widget=forms.Textarea, required=False, help_text='Optional: Complete a short description of item')
    photo = forms.ImageField(required=False, help_text='Opcional: load a photo of the item')

    

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['firstName', 'lastName', 'city', 'testimonial']
        
class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=60, required=True)
    last_name = forms.CharField(max_length=60, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, help_text="Enter a strong password.")
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, help_text="Enter the same password for confirmation.")

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2
            
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ["email","first_name", "last_name"]
        
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required= True)
       
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
    