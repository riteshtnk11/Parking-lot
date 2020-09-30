Plan of Action for NAS Academy Assignment 

Create a git repo for this assignment.
Create a server using python/django.
Server which can manage a parking lot.(API endpoints logic here).
Limit the IP address requests (No more than 10 requests from 1 ip in 10 seconds, if it does so “request cannot be processed” message).Will use django throttling for this.
Define one variable in the .env file as “parkingSlotSize” which the user can modify before starting the server.
Create a .Readme file that gives clear instructions on how to start the server and explains the solution.


For example:
slotNumbers: [1,2,3,4,5,6,......,12] (Editable via .env)
carNumbers: [11,12,13,14,15,16]


API Endpoints:
 parkCar(carNumber):
{
Method: Get
}
Conditions:
If input carNumber is invalid,display “Invalid car number;”
If the car is already parked, then return the slot number in which the car is parked.
If the car is not parked, then return the empty slots available to park a car.
If all slots are full, return that “all slots are full.Please wait for availability of slots”
	
unParkCar(slotNumber):
{
Method: Post
}
Conditions:
If input slotNumber is invalid,display “Invalid slot number;”
If input slotNumber is valid, then it will remove the parked car and update the parking slot details.
If the slot is already free then message “This slot is already free”

getInfo(carNumber/slotNumber):
{
Method: Get
}
Conditions:
If input carNumber is invalid,display “Invalid car number”
If input slotNumber is invalid,display “Invalid slot number”
If input carNumber is valid, then return the associated slot number along with the car number where it is parked, if not parked then return “car is not yet parked.”.
If input slotNumber is valid, then return the associated car number along with the number where it is parked, if no car is present at slot display “Input slot is empty”.


