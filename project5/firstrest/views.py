from django.shortcuts import render
from firstrest.models import Person
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from firstrest.serializers import PersonSerializer,AuthorSerializer
from firstrest.models import Author

# Create your views here.
def getPeople(request):
    result=Person.objects.all()
    return JsonResponse({'people': list(result.values())})

@api_view(['GET'])
def peopleList(request):
    result=Person.objects.all()
    serializer=PersonSerializer(result,many=True)
    return Response(serializer.data)


def view_home(request):
    authors=Author.objects.all()
    serializer=AuthorSerializer(authors,many=True)
    print(serializer.data)
    context={
        'authors': serializer.data
    }

    return render(request,'resthome.html',context)