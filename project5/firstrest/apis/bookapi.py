
from rest_framework.decorators import APIView
from firstrest.models import Author
from rest_framework.response import Response
from firstrest.serializers import AuthorSerializer

class AuthorAPI(APIView):
    def get(self,request,pk=None):
        if(pk==None):
            authors=Author.objects.all()
            result=AuthorSerializer(authors,many=True)
            return Response(result)
        return Response({'messsage':"Hello"})
