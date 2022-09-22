
from os import stat
from turtle import st
from rest_framework.decorators import APIView
from firstrest.models import Author
from rest_framework.response import Response
from firstrest.serializers import AuthorSerializer
from rest_framework import status

class AuthorAPI(APIView):
    def get(self,request,pk=None):
        if(pk==None):
            authors=Author.objects.all()
            print(list(authors.values()))
            result=AuthorSerializer(authors,many=True)
            return Response(result.data)
        else:
            try:
                author=Author.objects.get(pk=pk)
                return Response(AuthorSerializer(author).data)
            except Author.DoesNotExist:
                return Response({'error':'No Record'},status=status.HTTP_204_NO_CONTENT)

    def post(self,request):
        record=AuthorSerializer(data=request.data)
        try:
            if(record.is_valid()):
                record.save()
                return Response(record.data)
            else:
                return Response({'error':'Invalid Record'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
             return Response({'error':'Server Error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      

        

