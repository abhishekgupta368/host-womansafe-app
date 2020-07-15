from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .ApiViewset import LocationViewset

router = DefaultRouter()
router.register('locations', LocationViewset, basename = 'locations')

urlpatterns = [
    path("LogIn/",views.LogIn,name="LogIn"),
    path("complaint_locations/",views.get_complaint_location,name="complaint_locations"),
    path("home/",views.HomePage,name ="home"),
    path("signOut/",views.sign_out,name="signOut"),
    path('analysis_page/',views.analysisHome,name="analysis_page"),
    path('api/',include(router.urls),name='api'),# It is used to create view model data
]
