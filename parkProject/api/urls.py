from django.urls import path
from .views import index, park , unpark , slotinfo


urlpatterns=[
    path('',index,name='index'),
    path('park/', park.as_view()),
    # path('unpark/<slotNumber>/', unpark.as_view(),name='unpark'),
    path('unpark/<slotNumber>/', unpark.as_view()),
    path('slotinfo/<slotNumber>/', slotinfo.as_view()),
]