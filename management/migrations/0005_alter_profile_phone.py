# Generated by Django 5.0.6 on 2024-11-22 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_collection_country_vendor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]