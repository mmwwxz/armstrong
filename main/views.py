import random

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from main.models import Category, Product, Blog


def index(request):
    products = list(Product.objects.all())
    random_product = random.choice(products) if products else None

    return render(request, "index.html", {"random_product": random_product})


def catalog(request):
    # Get all products
    products = Product.objects.all()

    # Create paginator object with 9 items per page
    paginator = Paginator(products, 9)

    # Get page number from request, default to 1 if not provided
    page_number = request.GET.get('page', 1)

    # Get the Page object for the current page
    page_obj = paginator.get_page(page_number)

    # Group products into sets of three
    products_list = list(page_obj)
    products_groups = {
        'first_group': products_list[0:3] if len(products_list) > 0 else [],
        'second_group': products_list[3:6] if len(products_list) > 3 else [],
        'third_group': products_list[6:9] if len(products_list) > 6 else []
    }

    context = {
        'page_obj': page_obj,
        'products_groups': products_groups,
        'categories': Category.objects.all(),
    }
    return render(request, 'catalog.html', context)

def blog(request):
    # Get all blog posts
    blogs = Blog.objects.all().order_by('-created_at')

    # Create paginator object with 8 items per page (2 rows of 4 items)
    paginator = Paginator(blogs, 8)

    # Get page number from request, default to 1 if not provided
    page_number = request.GET.get('page', 1)

    # Get the Page object for the current page
    page_obj = paginator.get_page(page_number)

    # Group blogs into two rows of four
    blogs_list = list(page_obj)
    blogs_groups = {
        'first_group': blogs_list[0:4] if len(blogs_list) > 0 else [],
        'second_group': blogs_list[4:8] if len(blogs_list) > 4 else [],
    }

    context = {
        'page_obj': page_obj,
        'blogs_groups': blogs_groups,
    }
    return render(request, 'blog.html', context)


def contact(request):
    return render(request, 'contacts.html')


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Get random products excluding current product
    all_products = list(Product.objects.exclude(id=product_id))
    random_products = random.sample(all_products, min(len(all_products), 3))

    context = {
        'product': product,
        'random_product': random_products[0] if len(random_products) > 0 else None,
        'random_product2': random_products[1] if len(random_products) > 1 else None,
        'random_product3': random_products[2] if len(random_products) > 2 else None,
    }
    return render(request, 'detail.html', context)


def detail_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    return render(request, 'detail-blog.html', {'blog': blog})