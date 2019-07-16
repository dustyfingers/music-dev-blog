from django.shortcuts import render
from .models import Post


def posts(request):
    posts = Post.objects.order_by('-publish_date').filter(is_published=True)
    for post in posts:
        post.text = post.text[:200] + '...'
    context = {
        'posts': posts
    }
    return render(request, 'posts/posts.html', context)


def post(request):
    return render(request, 'posts/post.html')
