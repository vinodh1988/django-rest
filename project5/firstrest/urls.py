from django.urls import path,include
from firstrest.views import getPeople

urlpatterns=[
    path('list/',getPeople,name='people-list')
]