from rest_framework import serializers
from  firstrest.models import Person,Author,Book 

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    authorname=serializers.CharField(source='author.name',read_only=True)
    class Meta:
        model= Book
        fields = ('bookid','name','price','category','authorname')

    def validate(self,data):
            print(data)
            print(data['price'])
            if(data['price']<20):
                raise serializers.ValidationError('Price should be atleast Rs. 20')
            else:
                return data

class BookDirectSerializer(serializers.ModelSerializer):
    authorname=serializers.CharField(source='author.name',read_only=True)
    class Meta:
        model= Book
        fields = ('bookid','name','price','category','authorname','author')
        extra_kwargs={
            'author': {'write_only': True}
        }

    def validate(self,data):
            print(data)
            print(data['price'])
            if(data['price']<20):
                raise serializers.ValidationError('Price should be atleast Rs. 20')
            else:
                return data

    def validate_category(self, category):
        if( category not in ['Technology','Literature','Spiritual','Science','Biography']):
            raise serializers.ValidationError('Not a valid category')
        else:
            return category


        
class AuthorSerializer(serializers.ModelSerializer):
    books=BookSerializer(many=True)
    class Meta:
        model= Author
        fields = ('authorid','name','country','books')

    def create(self,validated_data):
        try:
            print('####this method is called')
            print(validated_data)
            temp_data = validated_data.pop('books')
            print(temp_data)
            author=Author.objects.create(**validated_data)
            for data in temp_data:
                Book.objects.create(author=author,**data)
            return author
        except Exception as e:
            print(e)