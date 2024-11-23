# Generated by Django 5.0.6 on 2024-11-22 03:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_remove_product_name_product_attributes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='add_stock',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='alt_text',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='updated',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='management.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='collections',
            field=models.ManyToManyField(blank=True, related_name='products', to='management.collection'),
        ),
        migrations.AddField(
            model_name='product',
            name='selected_countries',
            field=models.ManyToManyField(blank=True, related_name='products_in_country', to='management.country'),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='management.vendor'),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(default=2, upload_to='product_images/'),
            preserve_default=False,
        ),
    ]