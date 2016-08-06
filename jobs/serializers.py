from rest_framework import serializers

from .models import User, Place

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'user_name', 'email')

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ('place_name', 'country', 'city', 'lng', 'lat', 'image')