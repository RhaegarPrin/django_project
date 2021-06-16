# Generated by Django 3.1.7 on 2021-06-13 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0013_auto_20210612_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('iteem_name', models.CharField(max_length=100)),
                ('item_price', models.FloatField()),
                ('item_quantity', models.IntegerField()),
                ('item_note', models.CharField(max_length=1000)),
                ('item_tags', models.CharField(default=None, max_length=1000, null=True)),
                ('item_img', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
    ]
