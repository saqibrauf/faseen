# Generated by Django 2.1.2 on 2019-01-20 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circulars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='coupon',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='circulars.Coupon'),
        ),
    ]