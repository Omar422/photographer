# Generated by Django 3.2.7 on 2021-10-15 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_category_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='category/', verbose_name='صورة'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_image',
            field=models.ImageField(blank=True, null=True, upload_to='service', verbose_name='صورة'),
        ),
    ]