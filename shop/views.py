from math import ceil

from django.shortcuts import render

from .models import produts,contact_user

from django.http import HttpResponse


def index(request):
    allproducts = []
    cat_products = produts.objects.values('category', 'id')
    cats = {itemss['category'] for itemss in cat_products}

    for cat in cats:
        Products = produts.objects.filter(category=cat)
        n = len(Products)
        nslides = n // 4 + ceil((n // 4) - (n // 4))
        allproducts.append([Products, nslides])

    parms = {'allproducts': allproducts}

    return render(request, 'shop/index_html.html', parms)





def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        decs = request.POST.get('desc', '')
        print('\n',name,'\n', email,'\n', phone,'\n', decs)
        Contact = contact_user(name=name,email=email,phone=phone,decs=decs)
        Contact.save()

    return render(request, 'shop/contact.html')




def search(request):
    return render(request, 'shop/search.html')


def productview(request, myid):
    # fetch the product id
    Product = produts.objects.filter(id=myid)

    return render(request, 'shop/productview.html', {'Product': Product[0]})


def about(request):
    return render(request, 'shop/about.html')


def tracker(request):
    return render(request, 'shop/tracker.html')