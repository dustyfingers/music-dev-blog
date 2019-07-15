from django.shortcuts import render


def landing(request):
    return render(request, 'pages/landing.html')


def about(request):
    return render(request, 'pages/about.html')
