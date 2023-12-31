# Generated by Django 4.2.4 on 2023-08-13 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_ru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='_storage/media/ru/about/')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Certificates_ru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='_storage/media/ru/certificate/')),
            ],
        ),
        migrations.CreateModel(
            name='Contents_ru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Home_slaid_ru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='_storage/media/home/ru/')),
                ('title', models.CharField(max_length=99)),
                ('active', models.CharField(choices=[('no', 'no'), ('active', 'active')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Motto_ru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='_storage/media/ru/motto/')),
                ('name', models.CharField(max_length=250)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product_about_ru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product_ru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='_storage/media/ru/product/')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('two_images', models.ImageField(upload_to='_storage/media/ru/product/two/')),
            ],
        ),
        migrations.CreateModel(
            name='Statistika_ru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Video_ru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=250)),
                ('images', models.ImageField(upload_to='_storage/media/ru/video/')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
