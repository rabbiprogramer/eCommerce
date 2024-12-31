# Generated by Django 5.1.3 on 2024-12-30 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='area',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='full_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
