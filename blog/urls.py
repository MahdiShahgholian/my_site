from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_home_view, name = 'index'),
    path('search/', search_view, name='search'),
    path('<int:pid>', blog_single_view, name= 'single'),
    path('<str:cat_name>', blog_home_view, name= 'category'),
    path('<str:author_name>', blog_home_view, name= 'author'),
    path('tag/<str:tag_name>', blog_home_view, name= 'tag'),
]