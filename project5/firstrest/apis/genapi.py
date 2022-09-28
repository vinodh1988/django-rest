from firstrest.models import Author
from rest_framework import generics
from firstrest.serializers import AuthorSerializer

class AuthorGAPI(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer