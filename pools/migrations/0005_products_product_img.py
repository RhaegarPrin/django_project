# Generated by Django 3.1.7 on 2021-05-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0004_products_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_img',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
