from django.shortcuts import render
from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer

# Create your views here.

class CartListCreateView(generics.ListCreateAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    def delete(self,request,*args,**kwargs):
        Cart.objects.all().delete()
        return response(status=status.Http_204_NO_CONTENT)

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
