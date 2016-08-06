from rest_framework import generics, permissions
from jobs.views import UserViewSet

class UserList(UserViewSet, generics.ListAPIView):
	permission_classes = [
		permissions.AllowAny
	]