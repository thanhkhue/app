from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Place
from serializers import UserSerializer, PlaceSerializer
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import UserForm
from api.authentication import get_api_token
from django.http import Http404
from django.core.mail import send_mail

class PlaceViewSet(viewsets.ModelViewSet):
    model = Place
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST','GET'])
def register(request):
    api_token = get_api_token(request)
    tpl = "jobs/register.html"
    error = None
    message = None
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        user_serializer = UserSerializer(data = request.POST)
        print(request.POST)
        if user_serializer.is_valid():
            user = user_serializer.save()
            message = "Registration successfull"
            send_mail("test mail", "hello","thanhkhuebkdn2012@gmail.com",['shadowofdeath718@gmail.com'])
        else:
            error = "Your input is invalid. Please check, update and save again."
    context = {
        'api_token': api_token,
        'error': error,
        'message': message
    }
    return render(request, tpl, context)

