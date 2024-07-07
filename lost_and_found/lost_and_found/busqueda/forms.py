from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LostForm(forms.Form):
    when = forms.CharField(max_length=60)
    what = forms.CharField(max_length=60)
    where = forms.CharField(max_length=60)
    color = forms.CharField(max_length=50, required=False)
    model = forms.CharField(max_length=60, required=False)
    size = forms.CharField(max_length=60, required=False)
    
class FoundForm(forms.Form):
    when = forms.CharField(max_length=60)
    what = forms.CharField(max_length=60)
    where = forms.CharField(max_length=60)
    color = forms.CharField(max_length=50, required=False)
    model = forms.CharField(max_length=60, required=False)
    size = forms.CharField(max_length=60, required=False)

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['nombre', 'apellido', 'ciudad', 'testimonio']
        
class RegistroForm(UserCreationForm):
    firts_name = forms.CharField(max_length=60, min_length=3, required=True)
    last_name = forms.CharField(max_length=60, min_length=3, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Confirm password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2","firts_name", "last_name"]
    
