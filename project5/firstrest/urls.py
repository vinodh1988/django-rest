from django.urls import path,include
from firstrest.views import getPeople, peopleList
from firstrest.apis import AuthorAPI

urlpatterns=[
    path('list/',getPeople,name='people-list'),
    path('peoplelist/',peopleList),
    path('authors/',AuthorAPI.as_view(),name='author-list'),
    path('authors/<int:pk>',AuthorAPI.as_view(),name='author-by-id')
]