# Generated by Django 5.0.1 on 2024-02-20 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_comment_body_alter_comment_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/products_cover', verbose_name='Image'),
        ),
    ]
