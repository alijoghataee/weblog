from django.forms import ModelForm

from .models import Comment, Blog


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'recommend', )


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'text', 'cover', )
