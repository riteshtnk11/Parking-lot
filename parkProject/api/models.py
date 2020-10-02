from django.db import models
from django.urls import path






class CarDetail(models.Model):
    carNumber = models.CharField(max_length=10,null=False,blank=False,help_text='Enter the car number')    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.carNumber}  '

    
    def save(self, *args, **kwargs):
        self.carNumber = self.carNumber.upper()
        return super(CarDetail, self).save(*args, **kwargs)


class SlotDetail(models.Model):
    slotNumber = models.IntegerField(help_text='enter slot num',unique=True)
    carNumber = models.CharField(max_length=10,null=False,blank=False,help_text='Enter the car number') 
    created_at = models.DateTimeField(auto_now=True,)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.carNumber} parked in  slot no { self.slotNumber } on {self.created_at}'