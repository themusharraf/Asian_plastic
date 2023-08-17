from django.db import models


class Home_slaid(models.Model):
    images = models.ImageField(upload_to='_storage/media/home/en/')
    title = models.CharField(max_length=99)
    ACTIVE = (
        ('no', 'no'),
        ('active', 'active'),
    )
    active = models.CharField(choices=ACTIVE, max_length=50)


class Statistika(models.Model):
    name = models.CharField(max_length=250)
    number = models.IntegerField()


class About(models.Model):
    images = models.ImageField(upload_to='_storage/media/en/about/')
    text = models.TextField()


class Contents(models.Model):
    text = models.TextField()


class Motto(models.Model):
    images = models.ImageField(upload_to='_storage/media/en/motto/')
    name = models.CharField(max_length=250)
    text = models.TextField()


class Video(models.Model):
    link = models.CharField(max_length=250)
    images = models.ImageField(upload_to='_storage/media/en/video/')
    name = models.CharField(max_length=250)


class Product(models.Model):
    images = models.ImageField(upload_to='_storage/media/en/product/')
    title = models.CharField(max_length=250)
    text = models.TextField()
    two_images = models.ImageField(upload_to='_storage/media/en/product/two/')


class Product_about(models.Model):
    text = models.TextField()


class Certificates(models.Model):
    images = models.ImageField(upload_to='_storage/media/en/certificate/')
