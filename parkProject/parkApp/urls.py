from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from parkApp.views import *

urlpatterns = [
    # url(r'^hello-view/', views.HelloApiView.as_view()),
    # path('parkCar', parkCarAPI.as_view(), name='park'),
    # path('unparkCar', unparkCarAPI.as_view(), name='unpark'),
    path('parkInfo/', ParkInfo.as_view(), name='park_info'),
    path('parkCar/<str:carNumber>', parkCar.as_view(), name='park_car'),
    path('unParkCar/<int:slotNumber>', unParkCar.as_view(), name='unPark_car')
]

# urlpatterns = format_suffix_patterns(urlpatterns)