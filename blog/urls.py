from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [

    # /blog/create
    url(r'^create/$', views.BlogCreate.as_view(), name='create'),

    # /blog/blog-id/
    url(r'^(?P<pk>[0-9]+)/$', views.IndexView.as_view(), name='index'),

    # /blog/blog-id/3/
    url(r'^(?P<blog_id>[0-9]+)/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /blog/blog-id/3/comments
    url(r'^(?P<blog_id>[0-9]+)/(?P<pk>[0-9]+)/comments/$', views.CommentView.as_view(), name='comment'),

    # /blog/blog-id/3/comment
    url(r'^(?P<blog_id>[0-9]+)/(?P<post_id>[0-9]+)/comment/$', views.CommentCreate.as_view(), name='comment-add'),

    # /blog/blog-id/post/
    url(r'^(?P<blog_id>[0-9]+)/post/$', views.PostCreate.as_view(), name='post')
]
