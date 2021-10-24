# Generated by Django 3.2.7 on 2021-10-20 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20211020_1217'),
        ('portfolio', '0005_auto_20211015_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_category', to='service.category', verbose_name='القسم'),
        ),
    ]