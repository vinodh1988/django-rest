from rest_framework import serializers
from  firstrest.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields = '__all__'