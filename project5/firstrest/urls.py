from django.urls import path,include
from firstrest.views import getPeople, peopleList, view_home
from firstrest.apis import AuthorAPI,BookAPI

urlpatterns=[
    path('list/',getPeople,name='people-list'),
    path('peoplelist/',peopleList),
    path('authors/',AuthorAPI.as_view(),name='author-list'),
    path('authors/<int:pk>',AuthorAPI.as_view(),name='author-by-id'),
    path('books/',BookAPI.as_view(),name='book-list'),
    path('resthome/',view_home, name="view home page")
]