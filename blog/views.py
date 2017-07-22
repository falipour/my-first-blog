from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Weblog, Comment


class BlogCreate(CreateView):
    model = Weblog
    fields = ['author', 'blog_title']


class IndexView(generic.DetailView):
    model = Weblog
    template_name = 'blog/index.html'


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'


class CommentView(generic.DetailView):
    model = Post
    template_name = 'blog/comment.html'


class CommentCreate(CreateView):
    model = Comment
    fields = ['comment_text']

    def form_valid(self, form):
        post = None
        for post in Post.objects.all():
            if post.pk == int(self.kwargs['post_id']) and post.blog.pk == int(self.kwargs['blog_id']):
                post = post
        form.instance.post = post
        return super(CommentCreate, self).form_valid(form)


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'summary', 'post_text']

    def form_valid(self, form):
        weblog = None
        for blog in Weblog.objects.all():
            if blog.pk == int(self.kwargs['blog_id']):
                weblog = blog
        form.instance.blog = weblog
        return super(PostCreate, self).form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'summary', 'post_text']


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')
