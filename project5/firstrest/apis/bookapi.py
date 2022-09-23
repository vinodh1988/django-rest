

from rest_framework.decorators import APIView
from firstrest.models import Author,Book
from rest_framework.response import Response
from firstrest.serializers import AuthorSerializer,BookSerializer
from rest_framework import status
from rest_framework import serializers

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

    def put(self,request,pk):
        
        try:
            item=Author.objects.get(pk=pk)
            print(request.data)
            serialized=AuthorSerializer(item,data=request.data)
            if(serialized.is_valid()):
                serialized.save()
                return Response(serialized.data)
            else:
         
                return Response({'error':'Invalid Record'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
             return Response({'error':'Server Error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
   

class BookAPI(APIView):
    def get(self,request,pk=None):
        if(pk==None):
            books=Book.objects.all()
            print(list(books.values()))
            result=BookSerializer(books,many=True)
            return Response(result.data)
        else:
            try:
                book=Book.objects.get(pk=pk)
                return Response(AuthorSerializer(book).data)
            except Author.DoesNotExist:
                return Response({'error':'No Record'},status=status.HTTP_204_NO_CONTENT)

    def post(self,request):
        record=BookSerializer(data=request.data,read_only=True)
        print(record)
        print(record.initial_data)
        try:
            if(record.is_valid()):
                record.save()
                return Response(record.data)
            else:
                print("validation issue")
                return Response({'error':'Invalid Record'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except serializers.ValidationError as e:
            return Response({'error':e.message},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        except Exception as e:
             print('there is an exception')
             print(e.__class__)
             return Response({'error':'Server Error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      

        



