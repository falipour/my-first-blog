from django.db import models
from django.core.urlresolvers import reverse


class Weblog(models.Model):
    author = models.CharField(max_length=100)
    blog_title = models.CharField(max_length=1000)

    def get_absolute_url(self):
        print(self.pk)
        return reverse('blog:index', kwargs={'pk': self.pk})

    def __str__(self):
        return self.blog_title


class Post(models.Model):
    blog = models.ForeignKey(Weblog, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)
    post_text = models.TextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk, 'blog_id': self.blog.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=1000)
    comment_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.comment_text
