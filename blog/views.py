from django.shortcuts import get_object_or_404, render
from blog.models import Post, Author
#from models import *


def blog_list(request):
    blog = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'blog': blog})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/post_detail.html', {'post': post})
