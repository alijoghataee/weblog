from django.urls import path

from .views import *


urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', blog_detail_view, name='blog_detail'),
    path('blog/add/', create_blog_view, name='blog_create'),
    path('blog/search/', Search.as_view(), name='search'),
]
