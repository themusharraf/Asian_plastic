from django.db import models


class Home_slaid_ru(models.Model):
    images = models.ImageField(upload_to='_storage/media/home/ru/')
    title = models.CharField(max_length=99)
    ACTIVE = (
        ('no', 'no'),
        ('active', 'active'),
    )
    active = models.CharField(choices=ACTIVE, max_length=50)


class Statistika_ru(models.Model):
    name = models.CharField(max_length=250)
    number = models.IntegerField()


class About_ru(models.Model):
    images = models.ImageField(upload_to='_storage/media/ru/about/')
    text = models.TextField()


class Contents_ru(models.Model):
    text = models.TextField()


class Motto_ru(models.Model):
    images = models.ImageField(upload_to='_storage/media/ru/motto/')
    name = models.CharField(max_length=250)
    text = models.TextField()


class Video_ru(models.Model):
    link = models.CharField(max_length=250)
    images = models.ImageField(upload_to='_storage/media/ru/video/')
    name = models.CharField(max_length=250)


class Product_ru(models.Model):
    images = models.ImageField(upload_to='_storage/media/ru/product/')
    title = models.CharField(max_length=250)
    text = models.TextField()
    two_images = models.ImageField(upload_to='_storage/media/ru/product/two/')


class Product_about_ru(models.Model):
    text = models.TextField()


class Certificates_ru(models.Model):
    images = models.ImageField(upload_to='_storage/media/ru/certificate/')
