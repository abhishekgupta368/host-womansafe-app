from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .ApiViewset import LocationViewset

router = DefaultRouter()
router.register('locations', LocationViewset, basename = 'locations')

urlpatterns = [
    path('',views.LoadLogin,name=''),
    path("LogIn/",views.LogIn,name="LogIn"),
    path("complaint_locations/",views.get_complaint_location,name="complaint_locations"),
    path("home/",views.HomePage,name ="home"),
    path("signOut/",views.sign_out,name="signOut"),
    path('analysis_page/',views.analysisHome,name="analysis_page"),
    path('crime_rate/',views.return_states_counts,name="crime_rate"),
    path('registration/',views.register_to_system,name="registration"),
    path('delete_complaint/<int:id>',views.delete_complaint,name="delete_complaint"),
    path('api/',include(router.urls),name='api'),# It is used to create view model data
]
