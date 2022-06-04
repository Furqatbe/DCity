from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-info/', Getinfo),
    path('get-slider/', Getslider),
    path('get-projects/', Getprojects),
    path('get-technopark/', Gettechnopark),
    path('get-section/', Getsection),
    path('get-postalservices/', Getpostal),
    path('post-boglanish', Postboglanish),
    path('get-mobileoperators/', Getmobileoperators),
    path('get-internetproviders/', Getinternetproviders),
    path('get-ouraudience/', Getouraudience),
    path('get-percentage/', Getpercentage),
    path('get-residents/', Getresidents),
    path('get-team/', Getteam),
    path('get-coimages/', Getcoimages),
    path('get-coworking/', Getcoworking),
    path('get-infrastructure/', Getinfrastructure),
    path('get-studydirections/', Getstudydirections),
    path('get-itacademy/', Getitacademy),
    path('get-startupdirections/', Getstartupdirections),
    path('get-incubationcenters/', Getincubationcenters),
    path('get-raqamlashtirishchizmatlari/', Getraqamlashtirish),
    path('post-contact/', Postcontact),
    path('get-xizmatturi/', Getxizmatturi),
    path('get-xizmatlar/', Getxizmatlar),
    path('post-application', Postapplication)
]
