from rest_framework import serializers
from .models import Car, Parking


class CarSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model   = Car
        fields  = '__all__'
        depth   = 1
        
        
class ParkingSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model   = Parking
        fields  = '__all__'
        depth   = 1
