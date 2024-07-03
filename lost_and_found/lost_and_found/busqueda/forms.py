from django import forms
from .models import *

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
