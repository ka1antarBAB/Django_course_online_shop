# Generated by Django 5.0.1 on 2024-02-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/products_cover', verbose_name='Product Image'),
        ),
    ]