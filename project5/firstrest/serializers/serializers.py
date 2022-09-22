from rest_framework import serializers
from  firstrest.models import Person,Author

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields = '__all__'