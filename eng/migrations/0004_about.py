# Generated by Django 4.2.4 on 2023-08-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0003_statistika_alter_home_slaid_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='_storage/media/about/en/')),
                ('text', models.TextField()),
            ],
        ),
    ]
