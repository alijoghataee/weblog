from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Blog
from .forms import CommentForm, BlogForm


class BlogListView(generic.ListView):
    template_name = 'pages/blog_list_view.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(active=True)


@login_required
def blog_detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comment = blog.comment.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_form = comment_form.save(commit=False)
            new_form.blog = blog
            new_form.author = request.user
            new_form.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'pages/detail_blog.html', context={
        'blog': blog,
        'form': comment_form,
        'comment': comment
    })


def create_blog_view(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            new_form = blog_form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            return redirect('blog_list')
    else:
        blog_form = BlogForm()

    return render(request, 'pages/create_blog.html', context={
        'form': blog_form
    })


class Search(generic.ListView):
    model = Blog
    template_name = 'pages/blog_list_view.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        search = self.request.GET['q']
        return Blog.objects.filter(
            Q(title__contains=search) |
            Q(description__contains=search) |
            Q(active=True))
