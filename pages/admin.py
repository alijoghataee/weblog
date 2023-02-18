from django.contrib import admin

from .models import Blog, Comment, Categories


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog', 'active', )


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('categories', )
