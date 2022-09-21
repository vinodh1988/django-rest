from rest_framework import serializers
from  firstrest.models import Person

class PersonSerializer(serializers.Serializer):
    class Meta:
        model= Person
        fields = "__all___"