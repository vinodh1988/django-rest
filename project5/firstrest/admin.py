from django.contrib import admin
from .models import Person,Author,Book

# Register your models here.

admin.site.register(Person)
admin.site.register(Author)
admin.site.register(Book)