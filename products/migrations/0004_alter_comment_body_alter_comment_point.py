# Generated by Django 5.0.1 on 2024-02-20 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_comment_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='point',
            field=models.CharField(choices=[('1', 'very bad'), ('2', 'bad'), ('3', 'not bad'), ('4', 'good'), ('5', 'very good')], default='1', max_length=10, verbose_name='point'),
        ),
    ]
