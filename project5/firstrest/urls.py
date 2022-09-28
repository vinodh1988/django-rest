from django.urls import path,include
from firstrest.views import getPeople, peopleList, view_home,schema_view
from firstrest.apis import AuthorAPI,BookAPI
from firstrest.apis import AuthorGAPI,BookGAPI
urlpatterns=[
    path('list/',getPeople,name='people-list'),
    path('peoplelist/',peopleList),
    path('authors/',AuthorAPI.as_view(),name='author-list'),
    path('gauthors/',AuthorGAPI.as_view(),name='author-generic'),
    path('gbooks/',BookAPI.as_view(),name='book-generic'),
    path('authors/<int:pk>',AuthorAPI.as_view(),name='author-by-id'),
    path('books/',BookAPI.as_view(),name='book-list'),
    path('resthome/',view_home, name="view home page"),
    path('swagger/',schema_view)
]