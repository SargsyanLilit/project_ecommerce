# Generated by Django 3.2.9 on 2021-12-02 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
