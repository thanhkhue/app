from __future__ import unicode_literals
from django.db import models


class User(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	user_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	email = models.EmailField(max_length = 40)
	password = models.CharField(max_length = 100)
	activate = models.BooleanField(default=False)

	def __str__(self):
		return self.user_name

class Place(models.Model):
	place_name = models.CharField(max_length = 40)
	city = models.CharField(max_length = 25)
	country = models.CharField(max_length = 30)
	lng = models.DecimalField(max_digits=10,decimal_places=6)
	lat = models.DecimalField(max_digits=10,decimal_places=6)
	image = models.ImageField(upload_to = "static/jobs/image")

	def __unicode__(self):
		return "%s in %s" % (self.place_name, self.country)