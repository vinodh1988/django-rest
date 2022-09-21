from django.shortcuts import render
from firstrest.models import Person
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from firstrest.serializers import PersonSerializer

# Create your views here.
def getPeople(request):
    result=Person.objects.all()
    return JsonResponse({'people': list(result.values())})

@api_view(['GET'])
def peopleList(request):
    result=Person.objects.all()
    #serializer=PersonSerializer(result)
    return Response({'people': list(result.values())})