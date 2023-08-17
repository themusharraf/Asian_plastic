from django.shortcuts import render
from eng.models import *


def base(request):
    home = Home_slaid.objects.all()
    ctx = {
        'home':home
    }
    return render(request, 'en/base.html', ctx)


def index(request):
    home = Home_slaid.objects.all()
    statistika = Statistika.objects.all()
    about = About.objects.order_by('-id')[:1]
    con = Contents.objects.order_by('-id')[:1]
    motto = Motto.objects.all()
    video = Video.objects.order_by('-id')[:3]
    product = Product.objects.all()
    ctx = {
        'home': home,
        'statistika': statistika,
        'about': about,
        'con': con,
        'motto': motto,
        'video': video,
        'product': product
    }
    return render(request, 'en/index.html', ctx)


def Products(request):
    pro = Product.objects.all()
    prod = Product_about.objects.order_by('-id')[:1]
    ctx = {
        'pro': pro,
        'prod': prod
    }
    return render(request, 'en/blog.html', ctx)


def product_detail(request, id):
    product = Product.objects.filter(id=id).first()
    prok = Product.objects.all()
    ctx = {
        'product': product,
        'prok': prok
    }
    return render(request, 'en/product_detail.html', ctx)


def abouts(request):
    about = About.objects.order_by('-id')[:1]
    video = Video.objects.order_by('-id')[:3]
    ctx = {
        'about': about,
        'video': video,
    }
    return render(request, 'en/about.html', ctx)


def contact(request):
    return render(request, 'en/contact.html')


def Certificate(request):
    pro = Certificates.objects.all()
    ctx = {
        'pro': pro,
    }
    return render(request, 'en/Certificate.html', ctx)


def certificate_detail(request, id):
    product = Certificates.objects.filter(id=id).first()
    ctx = {
        'product': product
    }
    return render(request, 'en/detail.html', ctx)
