# Generated by Django 4.1.5 on 2023-02-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='123456qaz', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='номер телефона'),
        ),
    ]
