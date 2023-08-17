from django.shortcuts import render
from rus.models import *


def index_ru(request):
    home = Home_slaid_ru.objects.all()
    statistika = Statistika_ru.objects.all()
    about = About_ru.objects.order_by('-id')[:1]
    con = Contents_ru.objects.order_by('-id')[:1]
    motto = Motto_ru.objects.all()
    video = Video_ru.objects.order_by('-id')[:3]
    product = Product_ru.objects.all()
    ctx = {
        'home': home,
        'statistika': statistika,
        'about': about,
        'con': con,
        'motto': motto,
        'video': video,
        'product': product
    }
    return render(request, 'rus/index.html', ctx)


def Products_ru(request):
    pro = Product_ru.objects.all()
    prod = Product_about_ru.objects.order_by('-id')[:1]
    ctx = {
        'pro': pro,
        'prod': prod
    }
    return render(request, 'rus/blog.html', ctx)


def product_detail_ru(request, id):
    product = Product_ru.objects.filter(id=id).first()
    prok = Product_ru.objects.all()
    ctx = {
        'product': product,
        'prok': prok
    }
    return render(request, 'rus/product_detail.html', ctx)


def abouts_ru(request):
    about = About_ru.objects.order_by('-id')[:1]
    video = Video_ru.objects.order_by('-id')[:3]
    ctx = {
        'about': about,
        'video': video,
    }
    return render(request, 'rus/about.html', ctx)


def contact_ru(request):
    return render(request, 'rus/contact.html')


def Certificate_ru(request):
    pro = Certificates_ru.objects.all()
    ctx = {
        'pro': pro,
    }
    return render(request, 'rus/Certificate.html', ctx)


def certificate_detail_ru(request, id):
    product = Certificates_ru.objects.filter(id=id).first()
    ctx={
        'product':product
    }
    return render(request, 'rus/detail.html', ctx)
