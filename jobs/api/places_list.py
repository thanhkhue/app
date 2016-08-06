from rest_framework import generics, permissions
from jobs.views import PlaceViewSet

class PlaceList(PlaceViewSet, generics.ListAPIView):
	permission_classes = [
		permissions.AllowAny
	]