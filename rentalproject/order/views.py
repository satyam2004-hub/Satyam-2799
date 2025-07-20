from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def delete(self,request,*args,**kwargs):
        Order.objects.all().delete()
        return response(status=status.Http_204_NO_CONTENT)

