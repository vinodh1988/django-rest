
from rest_framework.decorators import APIView
from firstrest.models import Author
from rest_framework.response import Response
from firstrest.serializers import AuthorSerializer

class AuthorAPI(APIView):
    def get(self,request,pk=None):
        if(pk==None):
            authors=Author.objects.all()
            print(list(authors.values()))
            result=AuthorSerializer(authors,many=True)
            return Response(result.data)
        return Response({'messsage':"Hello"})

