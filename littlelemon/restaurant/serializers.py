#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
class BookingSerializer(serializers.ModelSerializer):
    model=Booking
    fields="__all__"
    