from django.db import models

# Create your models here.

# class car()
class Car(models.Model):
    carNumber       = models.CharField(max_length=200)
    slotNumber      = models.ForeignKey('Parking', on_delete=models.CASCADE)
    status          = models.CharField(default='parked',max_length=15)
    cerated_at      = models.DateTimeField(auto_now_add= True, null=True)
    updated_at      = models.DateTimeField(auto_now_add= True, null=True)

    def __str__(self):
        return self.carNumber
        
class Parking(models.Model):
    slotNumber      = models.IntegerField(unique=True)
    carNumber       = models.ForeignKey('Car', on_delete=models.CASCADE)
    status          = models.CharField(default='empty',max_length=15)
    cerated_at      = models.DateTimeField(auto_now_add= True, null=True)
    updated_at      = models.DateTimeField(auto_now_add= True, null=True)
    
    def __str__(self):
        return self.slotNumber