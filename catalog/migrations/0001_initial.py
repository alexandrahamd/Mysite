# Generated by Django 4.1.5 on 2023-01-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(default='', max_length=255, unique=True, verbose_name='URL')),
                ('content', models.CharField(blank=True, max_length=250, null=True)),
                ('preview', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]