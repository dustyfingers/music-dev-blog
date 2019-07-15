from django.shortcuts import render


def posts(request):
    return render(request, 'posts/index.html')


def post(request):
    return render(request, 'posts/post.html')
