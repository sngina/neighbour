from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import Neighbourhood , Business,User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name' , 'email')

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields=('name' ,'location' , 'occupants')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name' ,'email')