from django.shortcuts import render, get_object_or_404

from category.models import Category
from store.models import Product


def store(request, category_slug=None):

    print(category_slug)
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        # paginator = Paginator(products, 1)
        # page = request.GET.get('page')
        # paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        # paginator = Paginator(products, 3)
        # page = request.GET.get('page')
        # paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        # 'products': paged_products,
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)