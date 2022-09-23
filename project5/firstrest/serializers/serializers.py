from rest_framework import serializers
from  firstrest.models import Person,Author,Book 

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author=serializers.CharField(source='author.name')
    class Meta:
        model= Book
        fields = '__all__'
        def validate(self,data):
            if(data['price']<20):
                raise serializers.ValidationError('Price should be atleast Rs. 20')
    

class AuthorSerializer(serializers.ModelSerializer):
    books=BookSerializer(many=True,read_only=True)
    class Meta:
        model= Author
        fields = ('authorid','name','country','books')