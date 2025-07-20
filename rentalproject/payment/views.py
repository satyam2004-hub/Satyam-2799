from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer

# Create your views here.

class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer


    def delete(self,request,*args,**kwargs):
        Payment.objects.all().delete()
        return response(status=status.Http_204_NO_CONTENT)
