# Generated by Django 3.2.7 on 2021-10-23 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20211020_1217'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0004_auto_20211015_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date_request',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الطلب'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date_service',
            field=models.DateField(blank=True, verbose_name='تاريخ المناسبة'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='service.service', verbose_name='الخدمة'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('تحت الدراسة', 'تحت الدراسة'), ('مؤكد', 'مؤكد'), ('منفذ', 'منفذ')], default='underway', max_length=15, verbose_name='الحالة'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='المسخدم'),
        ),
    ]
