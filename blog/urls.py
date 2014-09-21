from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'blog.views.blog_list', name="blog-list"),
    url(r'^(?P<id>\d+)/$', 'blog.views.post_detail', name='post-detail'),
)
