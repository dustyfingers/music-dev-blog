from django.shortcuts import render, get_object_or_404
from .models import Post


def posts(request):
    posts = Post.objects.order_by('-publish_date').filter(is_published=True)
    for post in posts:
        post.text = post.text[:200] + '...'
    context = {
        'posts': posts
    }
    return render(request, 'posts/posts.html', context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post.html', context)
