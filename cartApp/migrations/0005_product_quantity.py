# Generated by Django 4.2.2 on 2023-07-13 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartApp', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]