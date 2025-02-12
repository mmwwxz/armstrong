from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def catalog(request):
    return render(request, 'catalog.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contacts.html')


def detail(request):
    return render(request, 'detail.html')


def detail_blog(request):
    return render(request, 'detail-blog.html')