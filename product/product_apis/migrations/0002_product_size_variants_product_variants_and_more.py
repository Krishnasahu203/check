# Generated by Django 5.1.3 on 2024-11-19 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Varient', '0004_sizevariant_product_sizevariant_shipping_cost_and_more'),
        ('product_apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size_variants',
            field=models.ManyToManyField(blank=True, related_name='products', to='Varient.sizevariant'),
        ),
        migrations.AddField(
            model_name='product',
            name='variants',
            field=models.ManyToManyField(blank=True, related_name='products', to='Varient.varient'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product_apis.productcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='isdisapproved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='relevent_Category_id',
            field=models.ManyToManyField(blank=True, to='product_apis.productcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_apis.productstatus'),
        ),
    ]