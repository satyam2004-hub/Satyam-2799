from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def delete(self,request,*args,**kwargs):
        Order.objects.all().delete()
        return response(status=status.Http_204_NO_CONTENT)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

