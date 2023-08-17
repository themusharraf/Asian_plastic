from django.urls import path
from eng.views import index, product_detail, Products, abouts, contact, certificate_detail, Certificate
from rus.views import index_ru, product_detail_ru, Products_ru, abouts_ru, contact_ru, certificate_detail_ru, Certificate_ru

urlpatterns = [
    path('', index, name='index'),
    path('Products', Products, name='Products'),
    path('product_detail/<str:id>/', product_detail, name='product'),
    path('about', abouts, name='about'),
    path('contact', contact, name='contact'),
    path('Certificate', Certificate, name='Certificate'),
    path('certificate_detail/<str:id>/', certificate_detail, name='certificate_detail'),

    # ru panel
    path('ru', index_ru, name='index_ru'),
    path('Products/ru', Products_ru, name='Products_ru'),
    path('product_detail/<str:id>/ru', product_detail_ru, name='product_ru'),
    path('about/ru', abouts_ru, name='about_ru'),
    path('contact/ru', contact_ru, name='contact_ru'),
    path('Certificate/ru', Certificate_ru, name='Certificate_ru'),
    path('certificate_detail/<str:id>/ru', certificate_detail_ru, name='certificate_detail_ru'),
]
