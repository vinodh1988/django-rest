from django.urls import path,include
from firstrest.views import getPeople, peopleList

urlpatterns=[
    path('list/',getPeople,name='people-list'),
    path('peoplelist/',peopleList)
]