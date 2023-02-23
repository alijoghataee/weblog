from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Blog, Comment, Categories
from .forms import CommentForm, BlogForm


class BlogListView(generic.ListView):
    template_name = 'pages/blog_list_view.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'pages/detail_blog.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        blog = Blog.objects.get(pk=self.kwargs['pk'])
        comment = blog.comment.filter(active=True)
        context['comment'] = comment
        context['form'] = CommentForm
        return context


class CommentCreatView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    success_message = "نظر شما با موفقیت ثبت شد و پس از تایید نمایش داده می شود"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        blog_pk = int(self.kwargs['pk'])
        blog = get_object_or_404(Blog, pk=blog_pk)
        obj.blog = blog

        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
        )


# def blog_detail_view(request, pk):
#     blog = get_object_or_404(Blog, pk=pk)
#     comment = blog.comment.filter(active=True)
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_form = comment_form.save(commit=False)
#             new_form.blog = blog
#             new_form.author = request.user
#             new_form.save()
#             comment_form = CommentForm()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, 'pages/detail_blog.html', context={
#         'blog': blog,
#         'form': comment_form,
#         'comment': comment
#     })


class CreateBlogView(SuccessMessageMixin, generic.CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'pages/create_blog.html'
    success_message = "مقاله شما با موفقیت ذخیره شد و بعد از تایید منتشر خواهد شد"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
        )


# def create_blog_view(request):
#     if request.method == 'POST':
#         blog_form = BlogForm(request.POST, request.FILES)
#         if blog_form.is_valid():
#             new_form = blog_form.save(commit=False)
#             new_form.author = request.user
#             new_form.save()
#             return redirect('blog_list')
#     else:
#         blog_form = BlogForm()
#
#     return render(request, 'pages/create_blog.html', context={
#         'form': blog_form
#     })


class Search(generic.ListView):
    template_name = 'pages/blog_list_view.html'
    context_object_name = 'blog'

    def get_queryset(self):
        blog = Blog.objects.filter(active=True)
        search = self.request.GET["q"]
        search_result = blog.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search))

        return search_result


class CategoriesListView(generic.ListView):
    model = Categories
    template_name = 'pages/categories_list.html'
    context_object_name = 'categories'


class BlogCategoriesView(generic.ListView):
    template_name = 'pages/blog_list_view.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        pk = self.kwargs['pk']
        blog = Blog.objects.filter(category=pk)
        return blog
