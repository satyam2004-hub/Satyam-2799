from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def delete(self,request,*args,**kwargs):
        Vehicle.objects.all().delete()
        return response(status=status.Http_204_NO_CONTENT)

