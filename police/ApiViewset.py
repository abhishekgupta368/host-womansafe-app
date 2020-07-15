from rest_framework import viewsets
from rest_framework.response import Response
from .models import Location
from .ApiSerializer import LocationSerializer

from rest_framework.response import Response
from rest_framework import status

class LocationViewset(viewsets.ModelViewSet):
    serializer_class  = LocationSerializer
    
    def get_queryset(self):
        location  = Location.objects.all()
        return location
    
    def retrieve(self,request,*args,**kwargs):
        pass

    def create(self,request,*args,**kwargs):
        location_serializer = LocationSerializer(data=request.data)
        if(location_serializer.is_valid()):
            location_serializer.save()
            return Response(location_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(location_serializer.data,status=status.HTTP_400_BAD_REQUEST)