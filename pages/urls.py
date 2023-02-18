from django.urls import path
from django.views.generic import TemplateView

from .views import *


urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/categories/', CategoriesListView.as_view(), name='categories'),
    path('blog/category/<int:pk>/', BlogCategoriesView.as_view(), name='blog_category'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('comment/<int:pk>/', CommentCreatView.as_view(), name='comment_create'),
    path('blog/add/', CreateBlogView.as_view(), name='blog_create'),
    path('blog/search/', Search.as_view(), name='search'),
    path('who-i-am-/', TemplateView.as_view(template_name='who_i_am.html'), name='who_i_am')
]
