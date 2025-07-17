from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import Users
from .serializers import UserSerializer

# Create your views here.
def create(request):
    return HttpResponse("This is a create page")

class UserCreateList(generics.ListCreateAPIView):
    queryset=Users.objects.all();
    serializer_class=UserSerializer;
    def delete(self,request,*args,**kwargs):
        Users.objects.all().delete()
        return response(status=status.Http_204_NO_CONTENT)


class USerUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
     queryset=Users.objects.all();
     serializer_class=UserSerializer;
     lookup_field="pk"


    