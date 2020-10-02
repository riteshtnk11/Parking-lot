import os
from django.shortcuts import render
from dotenv import load_dotenv
from django.http import Http404
from django.shortcuts import get_object_or_404

#rest_framework imports
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework import status
from rest_framework import throttling


#limiting the request
from rest_framework.throttling import AnonRateThrottle


#models import
from api.models import CarDetail,SlotDetail

#modelserializers
from .serializers import carSerializer,slotSerializer

#enviroment variable
load_dotenv()
lotsize = os.getenv('slotSize')


class UserMinThrottle(throttling.UserRateThrottle):
    scope = 'user_min'


@api_view(['GET'])
def index(request):
    api_endpoints = {
        'park':'localserver/park',
        'unpark':'localserver/unpark/slotNumber/',
        'slotinfo':'localserver/slotinfo/<slotNumber>/',
        'slotsize': lotsize

    }
    return Response(api_endpoints)


class park(APIView):
    throttle_classes = [UserMinThrottle]
    def post(self, request, format=None):
        serializer = slotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class unpark(APIView):
    def get(self, request,slotNumber):        
        queryset = SlotDetail.objects.get(slotNumber=slotNumber)
        serializer = slotSerializer(queryset)
        return Response(serializer.data)

    def get_object(self, slotNumber):
        try:
            return SlotDetail.objects.get(slotNumber=slotNumber)
        except SlotDetail.DoesNotExist:
            raise Http404
    
    def delete(self, request, slotNumber, format=None):
        slot = self.get_object(slotNumber)
        slot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class slotinfo(APIView):
    def get(self, request,slotNumber):        
        queryset = SlotDetail.objects.get(slotNumber=slotNumber)
        serializer = slotSerializer(queryset)
        return Response(serializer.data)
