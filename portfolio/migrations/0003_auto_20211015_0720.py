# Generated by Django 3.2.7 on 2021-10-15 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20211015_0701'),
        ('portfolio', '0002_auto_20211015_0701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='protfolio_title',
            new_name='portfolio_title',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='portfolio_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_category', to='service.category'),
            preserve_default=False,
        ),
    ]
