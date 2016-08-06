from django import forms
from .models import User, Place

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","user_name","email","password"]

class PlaceForm(forms.ModelForm):
	class Meta:
		model = Place
		fields = ['place_name', 'country', 'city', 'lng', 'lat', 'image']