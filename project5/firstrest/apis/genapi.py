from firstrest.models import Author
from rest_framework import generics
from firstrest.serializers import AuthorSerializer,BookSerializer,BookDirectSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import  filters

class AuthorGAPI(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name','country']
    search_fields = ['name','country']
    ordering_fields = ['name','country']

class BookGAPI(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = BookDirectSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name','price','author']
    search_fields = ['name','price','author']
    ordering_fields = ['name','price','author']