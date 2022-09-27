from django.shortcuts import render
from firstrest.models import Person
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from firstrest.serializers import PersonSerializer,AuthorSerializer
from firstrest.models import Author
from firstrest.forms import AuthorForm
from rest_framework_swagger.views import get_swagger_view

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
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()

    context={
        'authors': serializer.data,
        'form': AuthorForm()
    }

    return render(request,'resthome.html',context)


schema_view = get_swagger_view(title="Books API")