"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse
from django.shortcuts import HttpResponse, render
import book.views
from home import views as home_views


def index(request):
    # /book
    # print(reverse(book.views.book_query_string))

    # /book/str/1
    # print(reverse('book_str', kwargs={'book_id': 1}))

    # /movie/list
    # print(reverse('movie:movie_list'))

    return HttpResponse("Welcome to Alipu's DjangoProject")
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_views.index, name="home_views/index"),
    path('book/', book.views.book_query_string),
    # book_id 指定类型
    path('book/<int:book_id>', book.views.book_int),
    path('book/str/<str:book_id>', book.views.book_str, name='book_str'),
    path('book/slug/<slug:book_id>', book.views.book_slug),
    path('book/path/<path:book_id>', book.views.book_path),

    path('movie/', include('movie.urls')),
]
