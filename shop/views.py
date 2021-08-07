from math import ceil

from django.shortcuts import render

from .models import produts

from django.http import HttpResponse

# def index(request):
#     # return HttpResponse("Index shop")
#     cat_products = produts.objects.values('category', 'id')
#     print(cat_products)
#     Produts = produts.objects.all()
#     n = len(Produts)
#     nslides = n // 4 + ceil((n // 4) - (n // 4))
#     parms ={'no_of_slides':nslides,'range':range(1,nslides),'products':Produts}
#     allproducts = [[Produts, range(1, nslides), nslides], [Produts, range(1, nslides), nslides]]
#
#     parms = {'allproducts': allproducts}
#     return render(request, 'shop/index_html.html', parms)


#
def index(request):

    allproducts = []
    cat_products = produts.objects.values('category', 'id')
    # print('------cat products---------')
    # print(cat_products)

    cats = {itemss['category'] for itemss in cat_products}
    # print('-------cats--------')
    # print(cats)


    for cat in cats:
        Products = produts.objects.filter(category = cat)
        # print('--------Product-------')
        # print(Products)
        n = len(Products)
        nslides = n // 4 + ceil((n // 4) - (n // 4))
        allproducts.append([Products,nslides])
        # print('--------cat-------')
        # print(cat)


    parms = {'allproducts': allproducts}
    # print('------parst append---------')
    #
    # print(parms)
    return render(request, 'shop/index_html.html', parms)


def about(request):
    return render(request, 'shop/about.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def contact(request):
    return render(request, 'shop/contact.html')

def search(request):
    return render(request, 'shop/search.html')






