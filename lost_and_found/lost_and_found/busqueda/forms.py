from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

def clean_when(self):
        when = self.cleaned_data.get('when')

        # Verificar si la fecha es anterior o igual a la fecha actual
        if when > timezone.now().date():
            raise ValidationError('The date must be today or earlier')

        return when
    

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
    when = forms.DateField(input_formats=['%d/%m/%Y'],widget=forms.DateInput(format='%d/%m/%Y'), required=True, help_text='Format: dd/mm/aaaa', error_messages= {'required': 'Complete date'})
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
    first_name = forms.CharField(max_length=60, min_length=3, required=True)
    last_name = forms.CharField(max_length=60, min_length=3, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Confirm password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2","first_name", "last_name"]
        
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ["email","first_name", "last_name"]
        
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
    