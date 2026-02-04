from django.shortcuts import render, HttpResponse

# Create your views here

def movie_list(request):
    return HttpResponse("电影列表")

def movie_detail(request, movie_id):
    return HttpResponse(f"int 类型的电影id为{movie_id}")