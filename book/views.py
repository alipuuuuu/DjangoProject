from django.shortcuts import render, HttpResponse

# Create your views here.
# 1. 查询字符串方式: http:127.0.0.1:8000/book?id=3

# http://127.0.0.1:8000/book?id=4
def book_query_string(request):
    book_id = request.GET.get('id')
    book_name = request.GET.get('name')

    return HttpResponse(f"书本的id为 {book_id} <br>书本的名称为《{book_name}》")


"""
---------------------------------------------------------------------------------------------------------------------
"""
# # http://127.0.0.1:8000/book/1
def book_int(request, book_id):
    return HttpResponse(f"int 类型的id为 {book_id}")

# # http://127.0.0.1:8000/book/str
def book_str(request, book_id):
    return HttpResponse(f"str 类型的id为 {book_id}")

def book_slug(request, book_id):
    return HttpResponse(f"slug 类型的id为 {book_id}")

def book_path(request, book_id):
    return HttpResponse(f"path 类型的id为 {book_id}")