from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='blog_cover/')
    description = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    date_create = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title} : {self.author}'

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.id])


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    active = models.BooleanField(default=False)
    recommend = models.BooleanField("این مقاله را توصیه میکنم", default=True)
    blog = models.ForeignKey(Blog, related_name='comment', on_delete=models.CASCADE)

    Datetime_create = models.DateTimeField(auto_now_add=True)

