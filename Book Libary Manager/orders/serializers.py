from rest_framework import serializers
from .models import Order
from books.serializers import BookSerializer     
from users.serializers import UserSerializer     
class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)        
    book = BookSerializer(read_only=True)        
    class Meta:
        model = Order
        fields = ['id', 'user', 'book', 'quantity', 'status', 'created_at']
