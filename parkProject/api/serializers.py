#default imports
import os
from dotenv import load_dotenv
#models import
from .models import CarDetail , SlotDetail

#rest_framework import
from rest_framework.exceptions import ValidationError
from rest_framework import serializers


#enviroment variable
load_dotenv()
slotsize = os.getenv('slotSize')

class carSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDetail
        fields = '__all__'


class slotSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotDetail
        fields = '__all__'

    def validate(self, data):
        if len(data['carNumber']) < 10 :
            raise serializers.ValidationError({'carNumber':'carNumber must be 10 digits only ',
                                            'sample':'aa12bb1234'})
            
        elif SlotDetail.objects.all().count() == int(slotsize) :
            raise serializers.ValidationError({'slotNumber':'slotNumbers are occupied ','slotsize':slotsize})
        return data


        
