from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Post


def posts(request):
    posts = Post.objects.order_by('-publish_date').filter(is_published=True)
    for post in posts:
        post.text = post.text[:200] + '...'
    
    # pagination
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'posts': paged_posts
    }
    return render(request, 'posts/posts.html', context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post.html', context)
