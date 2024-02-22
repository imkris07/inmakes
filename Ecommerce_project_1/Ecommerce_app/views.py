from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def allprodcat(request, c_slug=None):
    c_page = None
    product_list= None

    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        product_list = Product.objects.all().filter(category=c_page, avaviable=True)
    else:
        product_list=Product.objects.all().filter(avaviable=True)

    paginator = Paginator(product_list, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page=1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': c_page, 'products': products})


def prodetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Product.DoesNotExist as e:
        raise e
    return render(request, 'product.html', {'Product': product})
