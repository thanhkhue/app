from django.contrib import admin
from .models import User, Place

class UserAdmin(admin.ModelAdmin):
    list_filter = ['user_name', ]
    search_fields = ['user_name', 'email']
    ordering = ['first_name', ]

    list_display = ('first_name', 'last_name', 'email')
    class Meta:
        model = User

class PlaceAdmin(admin.ModelAdmin):
	ordering = ['place_name',]
	search_fields = ['place_name']

admin.site.register(User,UserAdmin)
admin.site.register(Place,PlaceAdmin)