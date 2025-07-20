from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from booking.models import Booking
from .serializers import BookingSerializer

# Create your views here.
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def delete(self,request,*args,**kwargs):
        Booking.objects.all().delete()
        return response(status=status.Http_204_NO_CONTENT)
