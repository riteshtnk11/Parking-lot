from django.shortcuts import render

#rest frameworks imports
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

#Database model imports
from .models import Car, Parking

#Importing serializers below
from .serializers import CarSerializer, ParkingSerializer


# Create your views here.
class ParkInfo(APIView):
    
    def get(self, request, format=None):
        parking = Car.objects.all()
        serializer = CarSerializer(parking, many=True)
        return Response(serializer.data)

class parkCar(APIView):
    
    def get(self, request, carNumber=None):
        try:
            if Car.objects.filter(carNumber=carNumber).exists():
                return Response({"message":"Car exists and return slot number"}, status=200)
            else:
                # If slot is empty then park this car
                return Response({"message":"If slot is empty then park this car"}, status=202)
        except Car.DoesNotExist as e:
            return Response({"error":"Given car does not exists"}, status=404)
        
class unParkCar(APIView):
    
    def get(self, request, slotNumber=None):
        try:
            if Parking.objects.filter(slotNumber=slotNumber).exists():
                #if slot is empty then return "slot is already empty"
                #else remove the parked car
                return Response({"message":"Slot exists and return car number"}, status=200)
            else:
                return Response({"message":"slot does not exists"}, status=202)
        except Parking.DoesNotExist as e:
            return Response({"error":"Given sloW does not exists"}, status=404)