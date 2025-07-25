from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def delete(self,request,*args,**kwargs):
        Book.objects.all().delete()
        return response(status=status.Http_204_NO_CONTENT)


