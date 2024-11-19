# Generated by Django 5.1.3 on 2024-11-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SizeVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_with_shipping', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price (with shipping cost)')),
                ('add_size', models.BooleanField(default=False, verbose_name='Add Size Variant')),
                ('size', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Size Variant',
                'verbose_name_plural': 'Size Variants',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_variant', models.BooleanField(default=True)),
                ('enter_variant_name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='variant_images/')),
                ('variant_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]