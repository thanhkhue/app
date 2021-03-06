"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from jobs import views
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from jobs.api.user_list import UserList
from jobs.api.places_list import PlaceList
from django.conf.urls.static import static 
from django.conf import settings

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'places', views.PlaceViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/(?P<pk>[0-9]+)$', views.UserViewSet, name="userview"),
    url(r'^register', views.register, name="register"),
    url(r'^user_list', TemplateView.as_view(template_name='jobs/user_data.html'), name='user-list'),
    url(r'^place/(?P<pk>[0-9]+)$', views.PlaceViewSet, name="places"),
    url(r'^places_list', TemplateView.as_view(template_name='jobs/places_list.html'), name='places-list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

