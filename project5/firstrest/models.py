from django.db import models
from django.db.models import CheckConstraint

# Create your models here.

class Person(models.Model):
    sno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30,null=False)
    city=models.CharField(max_length=30,null=False)

    def __str__(self):
        return  str({'sno':self.sno,'name':self.name,'city':self.city})

class Author(models.Model):
    authorid=models.IntegerField(PrimaryKey=True)
    name=models.CharField(max_length=30,null=False)
    country=models.CharField(max_length=30,null=False)

    def __str__(self):
        return str({'authorid':self.authorid,'name':self.name,'country':self.country})

class Book(models.Model):
    bookid=models.IntegerField(PrimaryKey=True)
    name=models.CharField(max_length=30,null=False)
    price=models.FloatField(null=False)
    category=models.CharField(max_length=30,null=False)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books")

    def __str__(self):
        return str({'bookid':self.bookid,'name':self.name,'price':self.price,
        'category':self.category})

 
    