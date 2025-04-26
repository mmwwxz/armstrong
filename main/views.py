import random
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from main.models import Category, Product, Blog, HomePage, Info


def index(request):
    products = list(Product.objects.all())
    random_product = random.choice(products) if products else None
    random_product2 = random.choice(products) if products else None
    random_product3 = random.choice(products) if products else None

    home_page = HomePage.objects.first()

    context = {
        "random_product": random_product,
        "random_product2": random_product2,
        "random_product3": random_product3,
        "homepage": home_page
        }

    return render(request, "index.html", context)


def catalog(request):
    # Start with all products
    products = Product.objects.all()

    # Get filter parameters
    category_type = request.GET.get('category_type')
    subcategory = request.GET.get('subcategory')
    material_composition = request.GET.get('material_composition')
    region = request.GET.get('region')

    # Apply filters
    if category_type:
        # Filter by category type (lighting or ceilings)
        categories = Category.objects.filter(category_type=category_type)
        products = products.filter(category__in=categories)

    if subcategory:
        # Filter by specific subcategory name
        products = products.filter(category__name=subcategory)

    if material_composition:
        # Filter by material composition
        products = products.filter(material_composition=material_composition)

    if region:
        # Filter by region (material origin)
        products = products.filter(region=region)

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

    # Get all filter options for the template
    lighting_categories = Category.objects.filter(category_type='lighting')
    ceiling_categories = Category.objects.filter(category_type='ceilings')
    composition = Category.objects.filter(category_type='composition')
    material = Category.objects.filter(category_type='material')

    # Get unique material compositions and regions for filters
    # Using values_list with distinct to get unique values
    material_compositions = Product.objects.values_list('material_composition', flat=True).distinct()
    regions = Product.objects.values_list('region', flat=True).distinct()

    context = {
        'page_obj': page_obj,
        'products_groups': products_groups,
        'categories': Category.objects.all(),
        'lighting_categories': lighting_categories,
        'ceiling_categories': ceiling_categories,
        'material_compositions': material_compositions,
        'regions': regions,
        # Pass current filter settings to maintain state
        'current_category_type': category_type,
        'current_subcategory': subcategory,
        'current_material_composition': material_composition,
        'current_region': region,
    }
    return render(request, 'catalog.html', context)

def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 8)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    current_blogs = list(page_obj)
    blogs_groups = {
        'first_group': current_blogs[:4],
        'second_group': current_blogs[4:8]
    }

    context = {
        'page_obj': page_obj,
        'blogs_groups': blogs_groups,
    }

    return render(request, 'blog.html', context)


def contact(request):
    info = Info.objects.first()

    context = {
        "info": info,
    }

    return render(request, 'contacts.html', context)


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    category = product.category

    similar_products = Product.objects.filter(category=category).exclude(id=product_id)

    if similar_products.count() < 3:
        other_products = Product.objects.exclude(id=product_id).exclude(category=category)
        all_products = list(similar_products) + list(other_products)
    else:
        all_products = list(similar_products)

    import random
    random.shuffle(all_products)

    random_products = all_products[:min(len(all_products), 3)]

    context = {
        'product': product,
        'category': category,
        'random_product': random_products[0] if len(random_products) > 0 else None,
        'random_product2': random_products[1] if len(random_products) > 1 else None,
        'random_product3': random_products[2] if len(random_products) > 2 else None,
    }
    return render(request, 'detail.html', context)


def detail_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    return render(request, 'detail-blog.html', {'blog': blog})