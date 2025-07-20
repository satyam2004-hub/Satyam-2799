from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import Users
from .serializers import UserSerializers
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from users.serializers import UserSerializers

# Create your views here.
# def (request):
#     return HttpResponse("This is a create page")


class UserViewSet(viewsets.ModelViewSet):
     queryset=Users.objects.all();
     serializer_class=UserSerializers;
     permission_classes=[AllowAny]

     def delete(self,request,*args,**kwargs):
        Users.objects.all().delete()
        return response(status=status.Http_204_NO_CONTENT)