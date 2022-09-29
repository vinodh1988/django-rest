from rest_framework.pagination import PageNumberPagination

#class CursorPagination(CursorPagination):
 #   page_size = 5
   # ordering =


class BookPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param ='page_size'
    page_query_param= 'pageno'
    max_page_size=500