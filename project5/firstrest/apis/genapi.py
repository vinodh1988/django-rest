from firstrest.models import Author,Book
from rest_framework import generics
from firstrest.serializers import AuthorSerializer,BookSerializer,BookDirectSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import  filters
from firstrest.pagination import BookPagination
from rest_framework.permissions import IsAuthenticated

class AuthorGAPI(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name','country']
    search_fields = ['name','country']
    ordering_fields = ['name','country']

class BookGAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDirectSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name','price']
    search_fields = ['name','price']
    ordering_fields = ['name','price']
    ordering = 'bookid'
    pagination_class = BookPagination
   